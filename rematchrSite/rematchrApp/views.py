# rematchrApp/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Welcome to the Rematchr homepage")

def conference(request, conference_id):
	return HttpResponse("You're viewing a conference page")

def researcher(request, conference_id, researcher_id):
	return HttpResponse("You're viewing a researcher page")

def reviewer(request, conference_id, reviewer_id):
	return HttpResponse("You're viewing a reviewer page")


