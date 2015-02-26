# rematchrApp/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rematchrApp.models import Conference, Researcher, Reviewer

def index(request):
	conference_list = Conference.objects.order_by('id')
	context = {'conference_list': conference_list}
	return render(request, 'rematchrApp/index.html', context)	

def conference(request, conference_id):
	conference = get_object_or_404(Conference, pk=conference_id)
	context = {'conference': conference}
	return render(request, 'rematchrApp/conference.html', context) 

def researcher(request, conference_id, researcher_id):	
	conference = get_object_or_404(Conference, pk=conference_id)
	researcher = get_object_or_404(Researcher, pk=researcher_id)
	context = {'conference': conference, 'researcher': researcher}
	return render(request, 'rematchrApp/researcher.html', context)

def reviewer(request, conference_id, reviewer_id):
	conference = get_object_or_404(Conference, pk=conference_id)
	reviewer = get_object_or_404(Reviewer, pk=reviewer_id)
	context = {'conference': conference, 'reviewer': reviewer}
	return render(request, 'rematchrApp/reviewer.html', context)

