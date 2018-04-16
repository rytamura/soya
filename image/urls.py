from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('profile/<int:pk>/upload/', views.upload_view, name='image_upload'),
	path('profile/<int:pk>/browse/', views.browse_view, name='image_browse'),
]
