from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.personalHtml),
    url(r'^realAuth/$', views.realAuthHtml),
    url(r'^userInfo/$',views.userInfoHtml),
    url(r'^realAuth_upload/$',views.realAuth_upload)
 ]