from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^$', views.login, name='login'),
    url(r'^login$', auth_views.login , name='login'),
]