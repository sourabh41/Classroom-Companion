from django.conf.urls import url
<<<<<<< HEAD

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^$', views.login, name='login'),
    url(r'^login$', auth_views.login , name='login'),
]
=======
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.home,name='home'),
]
>>>>>>> a1aa13f0571cc4c8010b88a3b3cdeaf2cf026181
