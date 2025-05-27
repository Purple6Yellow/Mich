from django import forms
from django.forms import ModelForm
from .models import Contact

########## CONTACT FORMULIER #############
class Form_Co (forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {}
        widgets = {}
######## // CONTACT FORMULIER #############