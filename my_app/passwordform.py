from django.forms import ModelForm, widgets
from .models import passmanager

class passer(ModelForm):
	class Meta:
		model = passmanager
		fields = ['Website','Username','password']