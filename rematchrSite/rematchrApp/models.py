# rematchrApp/models.py

from django.contrib.auth.models import User
from django.db import models
import json

class Conference(models.Model):
	title = models.CharField(max_length=256)
	date = models.DateTimeField()
	user = models.ForeignKey(User, null=True)	 
		
	def __unicode__(self):
		return '%s' % self.title

class Researcher(models.Model):
	conference = models.ForeignKey(Conference)
	firstname = models.CharField(max_length=256)
	lastname = models.CharField(max_length=256)
	doc_texts = models.TextField(blank=True, default='')
	doc_urls = models.TextField(blank=True, default='')
	
	def set_doc_texts(self, texts):
		self.doc_texts = json.dump(texts)

	def get_doc_texts(self):
		return json.loads(self.doc_texts)	

	def set_doc_urls(self, urls):
		self.doc_urls = json.dump(urls)

	def get_doc_urls(self):
		return json.loads(self.doc_urls)	

	def __unicode__(self):
		return '%s, %s : %s' % (self.lastname, self.firstname, self.conference)

class Reviewer(models.Model):	
	conference = models.ForeignKey(Conference)
	firstname = models.CharField(max_length=256)
	lastname = models.CharField(max_length=256)	
	doc_texts = models.TextField(blank=True, default='')
	doc_urls = models.TextField(blank=True, default='')
	
	def set_doc_texts(self, texts):
		self.doc_texts = json.dump(texts)

	def get_doc_texts(self):
		return json.loads(self.doc_texts)	

	def set_doc_urls(self, urls):
		self.doc_urls = json.dump(urls)

	def get_doc_urls(self):
		return json.loads(self.doc_urls)	

	def __unicode__(self):
		return '%s, %s : %s' % (self.lastname, self.firstname, self.conference)
