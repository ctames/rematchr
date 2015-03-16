# rematchrApp/urls.py

from django.conf.urls import patterns, url
from rematchrApp import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^', views.index),
)


