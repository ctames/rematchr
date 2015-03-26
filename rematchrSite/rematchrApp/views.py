# rematchrApp/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rematchrApp.models import Conference, Researcher, Reviewer
from rematchrApp.forms import ConferenceForm
from django.contrib.auth.models import User

def index(request):
	return render(request, 'rematchrApp/index.html')

def account(request):	
	conferences = None
	if request.user.is_authenticated():
		conferences = request.user.conference_set.all()
	context = { 'conferences': conferences, }
	return render(request, 'rematchrApp/account.html', context)

def about(request):	
	return render(request, 'rematchrApp/about.html')

def conferenceAdd(request):
	id = 1
	try:
		id = Conference.objects.latest('id').id + 1
	except Conference.DoesNotExist:
		pass
	form = ConferenceForm()
	context = { "conferenceForm" : form, 'id' : id, }	
	return render(request, 'rematchrApp/create_conference.html', context)

def conferenceEdit(request, conference_id):
	conference = None
	if request.method == 'POST':
		form = ConferenceForm(request.POST)
		conference = form.save(commit=False)
		if request.user.is_authenticated():
			conference.user = request.user
		conference.save()
	else:
		conference = Conference.objects.get(id=conference_id)
		if request.user.is_authenticated():
			if conference.user != request.user:
				return render(request, 'rematchrApp/invalid_user.html')
	context = { "conference" : conference, }
	return render(request, 'rematchrApp/edit_conference.html', context)
