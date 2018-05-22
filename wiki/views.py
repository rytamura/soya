from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
from django.forms import ModelForm, HiddenInput
from django_file_md5 import calculate_md5
import os
import datetime

from geo.models import Feature, FeatureForm, RailroadStation2, RailroadSection2, Adm1920, Adm1950, Adm1995, Adm2015
from .geojson_serializer import Serializer
from .image_exif import ImageMetaData
from .models import WikiFile, WikiFileForm, WikiFileForm2, Article, ArticleForm

# Create your views here.

class MappedArticle:
	
	def __init__(self, pk, lat, lon, tit, author):
		self.pk = pk
		self.latitude=lat
		self.longitude=lon
		self.title = tit
		self.author = author

	def __str__(self):
		return "(%f, %f)" % [self.latitude, self.longitude]

class MappedFile:
	
	def __init__(self, pk, lat, lon, thumb, tit, summary):
		self.pk = pk
		self.latitude=lat
		self.longitude=lon
		self.img = thumb
		self.title = tit
		self.summary = summary
	def __str__(self):
		return "(%f, %f)" % [self.latitude, self.longitude]

		
def index(request):
	#
	articles = Article.objects.all()
	features = Feature.objects.all()
	files = WikiFile.objects.all()
	num_articles = Article.objects.count()
	num_features = Feature.objects.count()
	num_files = WikiFile.objects.count()

	maparts = [MappedArticle(a.pk, a.latitude, a.longitude, a.title, a.author) for a in articles if a.published and a.latitude]
	mapfiles = [MappedFile(f.pk, f.latitude, f.longitude, f.thumbL, f.title, f.summary) for f in files if f.published and f.latitude]

	return render(
		request,
		'wiki/index.html',
		context = {
			'maparts' : maparts,
			'mapfiles': mapfiles,
			'nart' : num_articles,
			'nfet' : num_features,
		}
	)

def features_view(request):
	points_as_geojson = serialize('custom_geojson', Feature.objects.all())
	return HttpResponse(points_as_geojson, content_type="json")


def filter_railways(gjobjects, from_year, to_year):
	return gjobjects.filter(
		Q(rail_name = '天北線') |
		Q(rail_name = '北見線') |
		Q(rail_name = '宗谷線') |
		Q(rail_name = '羽幌線') |
		Q(rail_name = '興浜北線') |
		Q(rail_name = '勇知線') |
		Q(rail_name = '幌沼線') |
		Q(company = '幌延町営軌道') |
		Q(company = '歌登町営軌道'),
	).exclude(
		operated_from__gt = to_year
	).exclude(
		operated_to__lt = from_year
	)

def layer_view(objs, from_year, to_year):
	ser = serialize('custom_geojson', filter_railways(objs, from_year, to_year))
	return ser

def stations_view(request, from_year=1900, to_year=2010):
	return HttpResponse(layer_view(RailroadStation2.objects, from_year, to_year), content_type="json")

def sections_view(request, from_year=1900, to_year=2010):
	return HttpResponse(layer_view(RailroadSection2.objects, from_year, to_year), content_type="json")

def adm1920_view(request):
	lines_as_geojson = serialize('custom_geojson', Adm1920.objects.filter(Q(sub_pref = '宗谷支庁') | Q(sub_pref='留萌支庁') | Q(city='中川村') ))
	return HttpResponse(lines_as_geojson, content_type="json")

def adm1950_view(request):
	lines_as_geojson = serialize('custom_geojson', Adm1950.objects.filter(Q(sub_pref = '宗谷支庁') | Q(sub_pref='留萌支庁') | Q(city='中川町') ))
	return HttpResponse(lines_as_geojson, content_type="json")

def adm1995_view(request):
	lines_as_geojson = serialize('custom_geojson', Adm1995.objects.filter(Q(sub_pref = '宗谷支庁') | Q(sub_pref='留萌支庁') | Q(city='中川町')))
	return HttpResponse(lines_as_geojson, content_type="json")

def adm2017_view(request):
	lines_as_geojson = serialize('custom_geojson', Adm2015.objects.filter(Q(sub_pref = '宗谷総合振興局') | Q(sub_pref='留萌振興局') | Q(city='中川町')))
	return HttpResponse(lines_as_geojson, content_type="json")

def wiki_media_dir(userid):
	upload_path = os.path.join(settings.MEDIA_ROOT, str(userid))
	if not os.path.exists(upload_path):
		os.mkdir(upload_path)
	return upload_path

def upload_view(request, pk):
	if request.method == 'POST':
		author = User.objects.get(pk=pk)
		if True: # form.is_valid():
			identity_check = WikiFile.objects.filter(md5 = calculate_md5(request.FILES.get('file')))
			if len(identity_check) > 0:
				return HttpResponse('このファイルは既に登録されています', status=500)

			file = request.FILES['file']
			upload_path = os.path.join(wiki_media_dir(request.user.id), file.name)
			#with open(upload_path, 'wb+') as dest:
			#	for chunk in file.chunks():
			#		dest.write(chunk)

			metadata = ImageMetaData(file.temporary_file_path())
			lat, lng = metadata.get_lat_lng()
			obj = WikiFile(created_at=datetime.datetime.now(), author=author, published=False, title="", summary="", latitude=lat, longitude=lng, upload=request.FILES.get('file'), md5=calculate_md5(request.FILES.get('file')))
			obj.save()
			return HttpResponse(status=200)
	else:
		return HttpResponse("Only POST methods needed", status=500)

	return HttpResponse("アップロードに失敗しました", status=500)

def list_files_view(request, pk):
	if request.method == 'POST':
		author = User.objects.get(pk=pk)
		objs = WikiFile.objects.filter(author=author)

	else:
		return HttpResponse("Only POST methods needed", status=500)

	return HttpResponse("アップロードに失敗しました", status=500)

def delete_uploaded_view(request, pk):
	if request.method == 'POST':
		uploaded = WikiFile.objects.filter(md5=calculate_md5)
		get_object_or_404(WikiFile, )
	else:
		return HttpResponse("Only POST methods needed", status=500)

	return HttpResponse('アップロードに失敗しました', status=500)

def edit_file(request, pk):
	userid = request.user.id
	file = WikiFile.objects.get(pk=pk)
	form = WikiFileForm2(instance=file)
	return render(
		request,
		'wiki/image_edit.html',
		context = {
			'userid' : userid,
			'form' : form,
			'file' : file
		}
	)

def update_file(request, pk):
	userid = request.user.id
	if request.method=="POST":
		file = WikiFile.objects.get(pk=pk)
		form = WikiFileForm2(request.POST, request)
		if form.is_valid():
			file.published = form.cleaned_data['published']
			file.title = form.cleaned_data['title']
			file.summary = form.cleaned_data['summary']
			file.categories.set(form.cleaned_data['categories'])
			file.latitude = form.cleaned_data['latitude']
			file.longitude = form.cleaned_data['longitude']
			file.save()
		else:
			raise
	else:
		return HttpResponse('Only POST method required', status=500)

	msg = {"msg": "アップデート完了!"}
	return HttpResponse(status=200)


def profile_view(request, pk):
	userid = request.user.id;
	wiki_media_dir(userid)	

	articles = Article.objects.filter(Q(author=request.user))
	files = WikiFile.objects.filter(Q(author=request.user))
	maparts = [MappedArticle(a.pk, a.latitude, a.longitude, a.title, a.author) for a in articles if a.latitude]

	return render(
		request,
		'wiki/profile.html',
		context={
			'userid' : userid,
			'name': request.user.get_username(),
			'articles': articles,
			'maparts': maparts,
			'files': files,
			'nart': articles.count(),
			'nfile': files.count(),
		}
	)

def get_gis_feature(params):
	if 'section' in params:
		return ['section', params['section']]
	elif 'station' in params:
		return ['station', params['station']]
	elif 'adm' in params:
		return ['adm', params['adm']]
	elif 'feature' in params:
		return ['feature', params['feature']]
	return ['UNKNOWN', 'UNKNOWN']

def create_article(request):
	if request.method == 'GET':
		gtype, feature_name = get_gis_feature(request.GET)
		lat = request.GET.get('lat')
		lng = request.GET.get('lng')
		form = ArticleForm(initial={'longitude':lng, 'latitude':lat, 'feature_name':feature_name, 'gis_type':gtype})
		new_feature = (gtype == "adm") and (lat is not None)
		is_adm = (gtype == "adm") and (lat is None)
		is_station = (gtype == "station")
		is_section = (gtype == "section")
		is_feature = (gtype == "feature")
		return render(
			request,
			'wiki/create.html',
			context = {
				'form': form,
				'userid': request.user.id,
				'feature': feature_name,
				'is_new': new_feature,
				'is_adm': is_adm,
				'is_station': is_station,
				'is_section': is_section,
				'is_feature': is_feature,
				'latitude': lat,
				'longitude': lng,
				'pk': 0, # not used
				'is_new': True
			}
		)
	else:
		return HttpResponse("UNNOWN METHOD APPLIED.", status=500)


def edit_article(request, pk):
	if request.method == 'GET': 
		art = Article.objects.get(pk=pk)
		gtype = art.gis_type
		feature_name = art.feature_name
		form = ArticleForm(instance=art)
		new_feature = (gtype == "adm") and (lat is not None)
		is_adm = (gtype == "adm") and (lat is None)
		is_station = (gtype == "station")
		is_section = (gtype == "section")
		is_feature = (gtype == "feature")
		return render(
			request,
			'wiki/create.html',
			context = {
				'form': form,
				'latitude': art.latitude,
				'longitude': art.longitude,
				'userid': request.user.id,
				'feature': feature_name,
				'is_new': new_feature,
				'is_adm': is_adm,
				'is_station': is_station,
				'is_section': is_section,
				'is_feature': is_feature,
				'pk':pk,
				'is_new': False
			}
		)
	else:
		return HttpResponse("UNNOWN METHOD APPLIED.", status=500)

def post_body(request, art, cl):
	art.published = cl['published']
	art.title = cl['title']
	art.summary = cl['summary']
	art.body = cl['body']
	art.feature_name = cl['feature_name']
	art.longitude = cl['longitude']
	art.latitude = cl['latitude']
	art.gis_type = cl['gis_type']
	art.period = cl['period']
	art.save()
	art.categories.set(cl['categories'])
	return HttpResponseRedirect(reverse('profile', args=(request.user.id, )))

def post_new_article(request, pk):
	if request.method == 'POST':
		form = ArticleForm(request.POST, request)
		if form.is_valid():
			user = User.objects.get(pk=request.user.id)
			art = Article(author=user)
			return post_body(request, art, form.cleaned_data)
		else:
			raise
	else:
		return HttpResponse("UNNOWN METHOD APPLIED.", status=500)

def post_article(request, pk):
	if request.method == 'POST':
		form = ArticleForm(request.POST, request)
		if form.is_valid():
			art = Article.objects.get(pk=pk)
			return post_body(request, art, form.cleaned_data)
		else:
			raise
	else:
		return HttpResponse("UNNOWN METHOD APPLIED.", status=500)

def view_article(request, pk):
	art = get_object_or_404(Article, pk=pk)
	return render (
		request,
		'wiki/view.html',
		context = {
			"art": art
		}
	)

def create_feature(request):
	params = request.GET
	adm = params['adm']
	latitude = params['lat']
	longitude = params['lng']
	form = FeatureForm(initial={'name':"", 'note':adm, 'latitude':latitude, 'longitude':longitude})
	#return HttpResponse(status=200)
	return render (
		request,
		'wiki/create_feature.html',
		context = {
			'form': form,
			'adm': adm,
			'latitude': latitude,
			'longitude': longitude,
		}
	)

def update_feature(request):
	params = request.POST
	userid = request.user.id
	form = FeatureForm(request.POST, request)
	if form.is_valid():
		feature = Feature.create(form.cleaned_data['name'], form.cleaned_data['note'], 
			form.cleaned_data['latitude'], form.cleaned_data['longitude'])
		feature.save()
	else:
		print(form)
		raise
	return HttpResponseRedirect(reverse('profile', args=(request.user.id, )))
