# rematchrApp/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rematchrApp.models import Conference, Researcher, Reviewer
from rematchrApp.forms import ConferenceForm

def index(request):
	return render(request, 'rematchrApp/index.html')

def account(request):
	return render(request, 'rematchrApp/account.html')

def about(request):
	return render(request, 'rematchrApp/about.html')

def conferenceAdd(request):
	form = ConferenceForm()
	context = { "conferenceForm" : form, }	
	return render(request, 'rematchrApp/create_conference.html', context)

def conferenceEdit(request):
	conference = None
	if request.method == 'POST':
		form = ConferenceForm(request.POST)
		conference = form.save(commit=False)
		conference.user = request.user
		conference.save()
	context = { "conference" : conference, }
	return render(request, 'rematchrApp/edit_conference.html', context)
