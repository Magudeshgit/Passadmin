from django.db import models
from django.contrib.auth.models import User
from fernet_fields import EncryptedField
from django.core.exceptions import ValidationError
from django.contrib import messages
from django import forms
# Create your models here.
# def urlvalid(value):
# 	if ".com" or ".ru" or ".org" or ".in" or ".net" or ".biz" or ".online" not in value:
# 		print("Err",type(value))
# 		raise ValidationError('The Website Name Must End with .com extension')
# 	else:
# 		return value

class passmanager(models.Model):
	frk = models.ForeignKey(User, related_name="Passodata", on_delete=models.CASCADE,  null=True)
	Website =  models.CharField(max_length=100, null=True)
	Username = models.CharField(max_length=100, null=True)
	password = EncryptedField(max_length=50)
	def __str__(self):
		return self.Website
		#, """widget=forms.TextInput(attrs={'class': 'int'})"""