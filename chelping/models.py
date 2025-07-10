from django.db import models
from django.utils import timezone
########## NIVEAU #############
NIVEAU = [
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
        #('2','3e klas'),
]),
    ('Vwo', [
        ('0','1e klas'),
        #('1','2e klas'),
]),
    ]
########## TRAINING #############
TRAINING =[
    ('KM', 'Kennismakingsgesprek'),
    ('RT', 'Remidial teaching'),
    ('LL', 'Leer Leren'),
]
########## LEEFTIJD #############
LEEFTIJD = [
    ('10', '10 jaar'),
    ('11', '11 jaar'),
    ('12', '12 jaar')
]

# CONTACTFORMULIER #
class Contact(models.Model):

  naam = models.CharField('naam', max_length=50,  blank=False, null = True )
  email = models.EmailField('email',unique=False,   blank=False, null = True)
  telefoon = models.CharField('telefoon', max_length=30, blank = False, null = True)
  volgorde = models.PositiveIntegerField(default=0)
  akkoord = models.BooleanField(default=False, null= False, blank = False)
  leeftijd = models.CharField(default = 'leeftijd', max_length = 50, choices = LEEFTIJD, blank = False, null = True)
  niveau = models.CharField (default = 'niveau', max_length = 50, choices = NIVEAU)
  training = models.CharField (default = 'training',  max_length= 50, choices = TRAINING)

  def __str__(self):
    return self.naam
  
  class Meta:
    ordering = ['volgorde']
    
#// CONTACTFORMULIER#

