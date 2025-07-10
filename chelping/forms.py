from django import forms
from django.forms import ModelForm
from .models import Contact


########## CONTACT FORMULIER #############
class Form_Co (forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['naam', 'niveau', 'email','telefoon', 'training', 'leeftijd'  ]
        labels = {  
            'naam': 'Naam:',
            'leeftijd':'Leeftijd',
            'niveau':'Niveau'} 
        widgets = {
            'naam': forms.TextInput (attrs={'class': 'form-select veld', 'placeholder': 'Naam',}),
            'email': forms.TextInput (attrs={'class': 'form-select veld', 'placeholder': 'Email'}),
            'telefoon': forms.TextInput (attrs={'class': 'form-select veld','placeholder': 'Telefoon',}),
            'leeftijd': forms.Select (attrs={'class': 'veld', 'placeholder': '??'}),
            'niveau': forms.Select (attrs={'class': 'veld1'}),
            'training': forms.Select (attrs={'class': 'veld1' })
            }
        
    def contact_mail(self):
        print('invulling van email')
        #invulling van email - verzonden via views.py
        naam= self.cleaned_data.get('naam','' )
        email = self.cleaned_data.get('email', 'niet doorgegeven')
        telefoon = self.cleaned_data.get('telefoon', 'niet doorgegeven')
        leeftijd = self.cleaned_data.get('leeftijd','')
        niveau = self.cleaned_data.get('niveau', '')
        training = self.cleaned_data.get('training','')

        return (
                f"Beste Michelle Degenaars,\n"
                f"Ik ben geinteresseerd in {training}.\n"
                f"Dit zijn mijn gegevens:\n\n"
                f"naam: {naam}\n"
                f"Mijn emailadres: {email}\n"
                f"Mijn telefoonnummer: {telefoon}\n\n"
                f"Mijn niveau is  {niveau}\n en ik ben {leeftijd} oud."
                f"Ik heb het privacy reglement "" gelezen" )
    
 

