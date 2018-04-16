from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Article
from geo.models import Feature, RailroadStation2, RailroadSection2, Adm1920, Adm1950, Adm1995, Adm2017
from django.http import HttpResponse
from django.core.serializers import serialize
from django.db.models import Q

# Create your views here.


def index(request):
	#
	num_articles = Article.objects.count()
	num_features = Feature.objects.count()

	return render(
		request,
		'wiki/index.html',
		context = {
			'nart' : num_articles,
			'nfet' : num_features,
		}
	)

def features_view(request):
	points_as_geojson = serialize('geojson', Feature.objects.all())
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
	return serialize('geojson', filter_railways(objs, from_year, to_year))

def stations_view(request, from_year=1900, to_year=2010):
	return HttpResponse(layer_view(RailroadStation2.objects, from_year, to_year), content_type="json")

def sections_view(request, from_year=1900, to_year=2010):
	return HttpResponse(layer_view(RailroadSection2.objects, from_year, to_year), content_type="json")

def adm1920_view(request):
	lines_as_geojson = serialize('geojson', Adm1920.objects.filter(Q(sub_pref = '宗谷支庁') | Q(sub_pref='留萌支庁') | Q(city='中川村') ))
	return HttpResponse(lines_as_geojson, content_type="json")

def adm1950_view(request):
	lines_as_geojson = serialize('geojson', Adm1950.objects.filter(Q(sub_pref = '宗谷支庁') | Q(sub_pref='留萌支庁') | Q(city='中川町') ))
	return HttpResponse(lines_as_geojson, content_type="json")

def adm1995_view(request):
	lines_as_geojson = serialize('geojson', Adm1995.objects.filter(Q(sub_pref = '宗谷支庁') | Q(sub_pref='留萌支庁') | Q(city='中川町')))
	return HttpResponse(lines_as_geojson, content_type="json")

def adm2017_view(request):
	lines_as_geojson = serialize('geojson', Adm2017.objects.filter(Q(sub_pref = '宗谷総合振興局') | Q(sub_pref='留萌振興局') | Q(city='中川町')))
	return HttpResponse(lines_as_geojson, content_type="json")

def profile_view(request, pk):
	userid = request.user.id;
	articles = Article.objects.filter(Q(author=request.user))
	return render(
		request,
		'wiki/profile.html',
		context={
			'name': request.user.get_username(),
			'articles': articles,
			'nart': articles.count()
		}
	)

def detail_view(request, pk):
	userid = request.user.id
	article = Article.objects.filter(Q(id=pk))
	return render(
		request,
		'wiki/detail.html',
		context = {
			'art': article,
		}
	)

def create_view(request, pk):
	pass


class DetailView(generic.DetailView):
	model=Article
	template_name = 'wiki/detail.html'

class CreateView(generic.CreateView):
	model = Article
	fields = '__all__'
	template_name = 'wiki/create.html'

class UpdateView(generic.UpdateView):
	model = Article
	fields = '__all__'
	exclude = ['author', 'soya_certified']
	template_name = 'wiki/update.html'

	def get_success_url(self):
		return reverse_lazy('profile', self.request.user.id)

class DeleteView(generic.DeleteView):
	model = Article
	success_url = reverse_lazy('wiki:index')
	template_name = 'wiki/delete.html'
 
def image_add_view(request):
	pass

"""	
def article_edit_view(request, pk):
	userid = request.user.id
	article = Article.objects.filter(Q(id=pk))
	return render (
		request,
		'wiki/update.html',
		context = {
			'art': article
		}
	)
"""