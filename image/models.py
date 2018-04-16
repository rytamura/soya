from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

class Image(models.Model):
	created_at =  models.DateTimeField(_('作成日'))
	uploaded_at = models.DateTimeField(_('アップロード日'))
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(_('名前'), max_length=64, null=False, default=_("image title"))
	desc = models.CharField(_('説明'), max_length=256, null=False, default=_("description"))
	longitude = models.FloatField(_('経度'), null=True)
	latitude = models.FloatField(_('緯度'), null=True)
