from django.conf.urls import url,include
from .import views
from django.views.generic import ListView
from posts.models import *

urlpatterns = [
    url(r'^$', views.post_home),
    url(r'^post_show/$', views.post_show),
    url(r'^post_create/$', views.post_create),
    url(r'^post_details/(?P<pk>\d+)$', views.post_details),
    url(r'^(?P<pk>\d+)/edit/$', views.post_update, name='post_update'),
    url(r'^value/(?P<pk>\d+)/$', views.post_value, name='post_value'),
    url(r'^post_list/$', ListView.as_view(queryset=Post.objects.all(), template_name="index.html")),
]
