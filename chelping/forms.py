from django import forms
from django.forms import ModelForm
from .models import Contact

########## CONTACT FORMULIER #############
NESTED_LAND = [
    ('Basisschool', [
        ('0','groep 3'),
        ('1','groep 4'),
        ('2','groep 5'),
        ('3','groep 6'),
        ('4','groep 7'),
        ('5','groep 8'),
]),
    ('Vmbo', [
        ('0','basis'),
        ('1','kader'),
        ('2','mavo'),
]),
    ('Havo', [
        ('0','1e klas'),
        ('1','2e klas'),
        ('2','3e klas'),
]),
    ('Vwo', [
        ('0','1e klas'),
        ('1','2e klas'),
]),
    ]

class Form_Co (forms.ModelForm):
    niveau = forms.ChoiceField(choices = NESTED_LAND)

    class Meta:
        model = Contact
        fields = ['naam', 'leeftijd', 'niveau', 'email','telefoon', 'training']
        labels = {  
            'naam':'',
            'leeftijd':'',}
        widgets = {
            'naam': forms.TextInput (attrs={'class': 'form-controle', 'placeholder': 'optioneel',}),}
######## // CONTACT FORMULIER #############

