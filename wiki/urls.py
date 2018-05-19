from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.flatpages import views as flatviews


urlpatterns = [
	# INDEX
	path('', views.index, name='index'),
	# GIS services
	path('features.data/', views.features_view, name='features'),
	path('stations.data/<int:from_year>/<int:to_year>', views.stations_view, name='stations'),
	path('sections.data/<int:from_year>/<int:to_year>', views.sections_view, name='sections'),
	path('adm1920.data/', views.adm1920_view, name='adm1920'),
	path('adm1950.data/', views.adm1950_view, name='adm1950'),
	path('adm1995.data/', views.adm1995_view, name='adm1995'),
	path('adm2017.data/', views.adm2017_view, name='adm2017'),
	# WikiFiles
	path('upload_files/<int:pk>', views.upload_view, name='upload_files'),
	path('list_files/<int:pk>', views.list_files_view, name='list_files'),
	path('delete_uploaded_file/<int:pk>/', views.delete_uploaded_view, name='delete_uploaded_files'),
	path('edit_file/<int:pk>', views.edit_file, name='edit_uploaded_file'),
	path('update_file/<int:pk>', views.update_file, name='update_uploaded_file'),
	# Prpfiles
	path('profile/<int:pk>/', views.profile_view, name='profile'),
	# Features
	path('create/feature/', views.create_feature, name='create_feature'),
	path('update/feature/', views.update_feature, name='update_feature'),
	# Article
	path('create/article/', views.create_article, name='create_article'),
	path('edit/article/<int:pk>', views.edit_article, name='edit_article'),
	path('post/article/<int:pk>/', views.post_article, name='post_article'),
	path('post/newarticle/<int:pk>/', views.post_new_article, name='post_new_article'),
	path('view/article/<int:pk>/', views.view_article, name='view_article'),
	# path('delete/article/<int:pk>/', views.DeleteView.as_view(), name='delete_article'),
	# Static Pages
	path('howto/', flatviews.flatpage, {'url': '/howto/', 'name': 'HowTo'}),
]
