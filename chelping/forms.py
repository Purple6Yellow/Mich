from django import forms
from django.forms import ModelForm
from .models import Contact

########## CONTACT FORMULIER #############
class Form_Co (forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {  
            'naam':'',
            'leeftijd':'',}
        widgets = {
               'naam': forms.TextInput (attrs={'class': 'form-controle', 'placeholder': 'optioneel',}),
               'leeftijd': forms.TextInput (attrs={'class': 'form-controle', 'placeholder': 'optioneel',}),
        }
######## // CONTACT FORMULIER #############

