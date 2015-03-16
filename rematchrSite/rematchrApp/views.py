# rematchrApp/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rematchrApp.models import Conference, Researcher, Reviewer

def index(request):
	return render(request, 'rematchrApp/index.html')



