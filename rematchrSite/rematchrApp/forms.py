# rematchrApp/forms.py

from django import forms
from rematchrApp.models import Conference

#http://stackoverflow.com/questions/4670783/make-the-user-in-a-model-default-to-the-current-user
class ConferenceForm(forms.ModelForm):
	class Meta:
		model = Conference
		exclude = ['user']



