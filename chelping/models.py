from django.db import models
from django.utils import timezone
########## NIVEAU #############
NIVEAU = [
    ('Basisschool', [
        ('basisschool:groep 3','groep 3'),
        ('basisschool:groep 4','groep 4'),
        ('basisschool:groep 5','groep 5'),
        ('basisschool:groep 6','groep 6'),
        ('basisschool:groep 7','groep 7'),
        ('basisschool:groep 8','groep 8'),
]),
    ('Vmbo', [
        ('vmbo:basis','basis'),
        ('vmbo:kader','kader'),
        ('vmbo:mavo','mavo'),
]),
    ('Havo', [
        ('havo 1e klas','1e klas'),
        ('havo, 2e klas','2e klas'),
        #('2','3e klas'),
]),
    ('vwo', [
        ('vwo, 1e klas','1e klas'),
        #('1','2e klas'),
]),
    ]
########## TRAINING #############
TRAINING =[
    ('een kennismakingsgesprek', 'Kennismakingsgesprek'),
    ('de Remidial Teaching training', 'Remidial teaching'),
    ('de training "Ik leer leren"', 'Leer Leren'),
]
########## LEEFTIJD #############
LEEFTIJD = [
    ('5', '5 jaar'),
    ('6', '6 jaar'),
    ('7', '7 jaar'),
    ('8', '8 jaar'),
    ('9', '9 jaar'),
    ('10', '10 jaar'),
    ('11', '11 jaar'),
    ('12', '12 jaar'),
    ('13', '13 jaar'),
    ('14', '14 jaar'),
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

