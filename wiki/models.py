from django.db import models
from django import forms
from django.forms import ModelForm, HiddenInput
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from tinymce.models import HTMLField
from tinymce import models as tinymce_models
from tinymce.widgets import TinyMCE
import os

from geo.models import Feature

# Create your models here.

class Period(models.Model):
	name = models.CharField(max_length=32)
	def __str__(self):
		return(self.name)

def default_period():
	return Period.objects.get_or_create(name='年代なし')

class Category(models.Model):
	name = models.CharField(max_length=32)
	def __str__(self):
		return(self.name)
def default_category0():
	category, _ = Category.objects.get_or_create(name='未分類')
	return category

def default_category_m2m():
	return default_category0(), 

class Article(models.Model):
	created_at = models.DateTimeField('作成日時', auto_now_add=True)
	updated_at = models.DateTimeField('更新日時', auto_now=True)
	# draft or publish
	published = models.BooleanField('公開する', default=False)
	feature_name = models.CharField(max_length=128, default="No place")
	gis_type = models.CharField(max_length=32, default="No GIS type")
	period = models.ForeignKey(Period, on_delete=models.PROTECT, verbose_name='年代', null=True)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField('記事タイトル', max_length=48)
	summary = models.CharField('記事の概要', max_length=128)
	body = tinymce_models.HTMLField('本文')
	feature = models.ForeignKey(Feature, on_delete=models.PROTECT, null=True)
	categories = models.ManyToManyField(Category, verbose_name="カテゴリ")
	soya_certified = models.BooleanField(_("認証済"), default=False, help_text=_("Certified"))

	class Meta:
		ordering = ["-updated_at"]

	def __str__(self):
		return(("Article: ") + self.title)

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ('published', 'title', 'summary', 'body', 'categories', 'feature_name', 'longitude', 'latitude', 'gis_type', 'period')
		widgets = {'feature_name': HiddenInput(), 'longitude': HiddenInput(), 'latitude': HiddenInput(), 'gis_type': HiddenInput()}

class Comment(models.Model):
	created_at = models.DateTimeField('作成日時', auto_now=True)
	updated_at = models.DateTimeField('更新日時', auto_now=True)

	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	body = models.TextField('本文')
	comment_to = models.ForeignKey(Article, on_delete=models.PROTECT, null=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return("Comment")


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'


def user_directory_path(instance, filename):
	return os.path.join(str(instance.author.id), filename)

class WikiFile(models.Model):
	created_at = models.DateTimeField('アップロード日時', auto_now_add=True)
	author = models.ForeignKey(User, '投稿者', default=False)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	published = models.BooleanField('公開', default=False)
	title = models.CharField('タイトル', max_length=128, default="")
	summary = models.CharField('概要', max_length=256, default="")
	categories = models.ManyToManyField(Category, default=default_category_m2m, verbose_name="カテゴリ")
	md5 = models.CharField('md5', max_length=32, default="", null=False)

	upload = models.ImageField('画像や写真', upload_to=user_directory_path, null=False)
	thumbL = ImageSpecField(source="upload", processors=[ResizeToFill(1280, 1024)],format='JPEG')
	thumbM = ImageSpecField(source="upload", processors=[ResizeToFill(640, 480)],format='JPEG', options={'quality':75})
	thumbS = ImageSpecField(source='upload', processors=[ResizeToFill(100,100)],format="JPEG",options={'quality':60})

	class Meta:
		ordering = ["-created_at"]

class WikiFileForm(ModelForm):
	class Meta:
		model = WikiFile
		fields = ['upload']

class WikiFileForm2(ModelForm):
	class Meta:
		model = WikiFile
		fields = ['published', 'title', 'summary', 'categories', 'longitude', 'latitude']
		widgets = {'longitude': HiddenInput(), 'latitude': HiddenInput()}

				




