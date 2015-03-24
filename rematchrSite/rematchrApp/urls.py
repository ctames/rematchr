# rematchrApp/urls.py

from django.conf.urls import patterns, url
from rematchrApp import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^account$', views.account, name='account'),
	url(r'^about', views.about, name='about'),
	url(r'^account/newconf/', views.conferenceAdd, name='newconf'),
	url(r'^account/editconf/', views.conferenceEdit, name='editconf'),
)


