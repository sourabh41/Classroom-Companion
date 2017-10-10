from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^addcourse/$', views.add_course, name = 'addcourse'),
    url(r'^makecourse$', views.make_course, name = 'makecourse'),
    url(r'^addstudents/$', views.add_students_to_course1, name = 'addstudents'),
    url(r'^csv$', views.add_students_to_course2, name = 'csvfile')
]

