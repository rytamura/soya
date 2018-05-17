from django.contrib import admin
from .models import Category, Article, Comment, WikiFile, Period

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(WikiFile)
admin.site.register(Comment)
admin.site.register(Period)



