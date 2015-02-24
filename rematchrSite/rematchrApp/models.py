from django.db import models
import json

class Conference(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField()	

	def __unicode__(self):
		return self.title

class Researcher(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	conference = models.ForeignKey(Conference)
	doc_texts = models.TextField()
	doc_urls = models.TextField()
	
	def set_doc_texts(self, texts):
		self.doc_texts = json.dump(texts)

	def get_doc_texts(self):
		return json.loads(self.doc_texts)	

	def set_doc_urls(self, urls):
		self.doc_urls = json.dump(urls)

	def get_doc_urls(self):
		return json.loads(self.doc_urls)	

	def __unicode__(self):
		return self.lastname + ", " + self.firstname + " : " + self.conference

class Reviewer(models.Model):	
	conference = models.ForeignKey(Conference)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)	

	def __unicode__(self):
		return self.lastname + ", " + self.firstname + " : " + self.conference
