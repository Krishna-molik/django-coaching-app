from django import forms
from .models import UserDetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
class ReviewForm(forms.ModelForm):
	class Meta:
		model = UserDetails
		fields = ['text','Photo']

class SignUpForm(UserCreationForm):
	MobileNo = forms.CharField(max_length=10, validators=[
		RegexValidator(
			regex = r'^[6-9]/d{9}$',
			message = "Enter a valid Mobile Number"
			)
		])
	class Meta:
		model = User
		fields = ('username','MobileNo','password1','password2')

