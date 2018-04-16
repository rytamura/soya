from django.urls import path
from . import views
from django.contrib.flatpages import views as flatviews


urlpatterns = [
	path('', views.index, name='index'),
	path('features.data/', views.features_view, name='features'),
	path(r'stations.data/<int:from_year>/<int:to_year>', views.stations_view, name='stations'),
	path(r'sections.data/<int:from_year>/<int:to_year>', views.sections_view, name='sections'),
	path('adm1920.data/', views.adm1920_view, name='adm1920'),
	path('adm1950.data/', views.adm1950_view, name='adm1950'),
	path('adm1995.data/', views.adm1995_view, name='adm1995'),
	path('adm2017.data/', views.adm2017_view, name='adm2017'),
	path('profile/<int:pk>/', views.profile_view, name='profile'),
	path('create/article/<int:pk>/', views.CreateView.as_view(), name='create_article'),
	path('show/article/<int:pk>/',   views.DetailView.as_view(), name='show_article'),
	path('update/article/<int:pk>/', views.UpdateView.as_view(), name='update_article'),
	path('delete/article/<int:pk>/', views.DeleteView.as_view(), name='delete_article'),
	path('howto/', flatviews.flatpage, {'url': '/howto/', 'name': 'HowTo'}),
]
