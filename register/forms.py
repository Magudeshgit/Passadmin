from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	image = forms.ImageField(required=True,label="Your Profile")
	class Meta:
		model = User
		fields = ["username", "image","first_name","last_name","email","password1", "password2"]
class LoginForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ["username", "password1"]