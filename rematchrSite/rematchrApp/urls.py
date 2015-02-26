# rematchrApp/urls.py

from django.conf.urls import patterns, url
from rematchrApp import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^conferences/(?P<conference_id>\d+)/$', views.conference, name='conference'),
	url(r'^conferences/(?P<conference_id>\d+)/researchers/(?P<researcher_id>\d+)/$',
		views.researcher, name='researcher'),
	url(r'^conferences/(?P<conference_id>\d+)/reviewers/(?P<reviewer_id>\d+)/$',
		views.reviewer, name='reviewer'),
)


