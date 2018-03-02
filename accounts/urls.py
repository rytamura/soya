from django.urls import include, path
from django.contrib.auth.views import login,logout

from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', login,
        {'template_name': 'accounts/login.html'},
        name='login'),
    path('logout/', logout,
    	{'template_name': 'accounts/logout.html'},
    	 name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]