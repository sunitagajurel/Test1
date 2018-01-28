from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    path('',views.home,name ='home'),
    path('login/',login,{'template_name':'accounts/login.html'},name='login'),
    path('logout/',logout,{'template_name':'accounts/logout.html'},name='logout'),
    path('register/',views.register,name='register'),
   	url(r'^profile/$',views.profile,name='profile')
]