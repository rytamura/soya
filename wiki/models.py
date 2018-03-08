from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from geo.models import Feature
from django.utils.translation import gettext as _

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=32)
	def __str__(self):
		return(self.name)


class Article(models.Model):
	created_at = models.DateTimeField('作成日時', auto_now=True)
	updated_at = models.DateTimeField('更新日時', auto_now=True)
	# draft or publish
	published = models.BooleanField('公開', default=False)

	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField('タイトル', max_length=128)
	summary = models.CharField('概要', max_length=256)
	body = models.TextField('本文')
	landmark = models.ForeignKey(Feature, on_delete=models.PROTECT, null=True)
	categories = models.ManyToManyField(Category)
	soya_certified = models.BooleanField(_("認証済"), default=False, help_text=_("Certified"))

	class Meta:
		ordering = ["-updated_at"]

	def __str__(self):
		return(("Article: ") + self.title)

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'
		exclude = ['soya_certified']


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


class Image(models.Model):
	created_at = models.DateTimeField('作成日時', auto_now=True)
	updated_at = models.DateTimeField('更新日時', auto_now=True)
	published = models.BooleanField('公開', default=False)

	title = models.CharField('タイトル', max_length=128, default="")
	summary = models.CharField('概要', max_length=256, default="")
	landmark = models.ForeignKey(Feature, on_delete=models.PROTECT, null=True)
	categories = models.ManyToManyField(Category)
	upload = models.ImageField('画像', upload_to="uploads", null=True)

	class Meta:
		ordering = ["-created_at"]
