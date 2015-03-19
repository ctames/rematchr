from django import forms

class ConferenceAddForm(forms.ModelForm):
	class Meta:
		model = Conference 
