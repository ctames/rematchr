# rematchrApp/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rematchrApp.models import Conference, Researcher, Reviewer
from forms import ConferenceAddForm


def index(request):
	return render(request, 'rematchrApp/index.html')

def account(request):
	return render(request, 'rematchrApp/account.html')

def about(request):
	return render(request, 'rematchrApp/about.html')


#http://stackoverflow.com/questions/4670783/make-the-user-in-a-model-default-to-the-current-user	
def conferenceAdd(request):
	form = ConferenceAddForm(request.POST)
	if form.is_valid():
		Conference = form.save(commit=False)
		Conference.user = request.user
		Conference = Conference.save()
	





