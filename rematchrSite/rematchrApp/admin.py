from django.contrib import admin
from rematchrApp.models import Conference, Researcher, Reviewer 

class ResearcherInline(admin.TabularInline):
	model = Researcher

class ReviewerInline(admin.TabularInline):
	model = Reviewer  

class ConferenceAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')
	inlines = [ResearcherInline, ReviewerInline]	

admin.site.register(Conference, ConferenceAdmin)


