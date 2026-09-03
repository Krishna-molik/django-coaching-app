from django import forms
from .models import UserDetails

class ReviewForm(forms.ModelForm):
	class Meta:
		model = UserDetails
		fields = ['text','Photo']
