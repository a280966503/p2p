from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^register/$', views.register),
    url(r'^registerNameCheck/$', views.registerNameCheck),
    url(r'^registerSubmit/$', views.registerSubmit),
    url(r'^login/$', views.login),
    url(r'^loginSubmit/$', views.loginSubmit)
 ]