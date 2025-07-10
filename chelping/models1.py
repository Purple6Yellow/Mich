from django.db import models
from django.utils import timezone


# CONTACTFORMULIER#

class Interesse(models.Model):
  leeftijd = models.CharField(max_length=100, choices=[  ('0','basisschool'),
  ('1','vmbo'),
  ('2','havo'),
  ('3','vwo'),])

  def __str__(self):
    return self.leeftijd
  
class Gebruiker(models.Model):
  leeftijd = models.CharField(max_length =100)
  interesses=models.ManyToManyField(Interesse)


NIV_CHOICES= [
  ('0','basisschool'),
  ('1','vmbo'),
  ('2','havo'),
  ('3','vwo'),
]

TRAIN_KEUZE = [('RT','Remidial Teaching'),  ('LL','Leer Leren'),  ('NL', 'Nederlands'),('FA','Faalangst training')]

class Contact(models.Model):
  naam = models.CharField('naam', max_length=50,  blank=False, null = True)
  niveau = models.CharField(max_length=30,blank=False, choices=NIV_CHOICES, default = 'onbekend')
  email = models.EmailField('email',unique=False,   blank=False, null = True)
  telefoon = models.CharField('telefoon', max_length=30, blank = False, null = True)
  akkoord = models.BooleanField(default=False, null= False, blank = False)
  training = models.CharField(max_length=30,default = 'Onbekend',blank=False, null = True, choices=TRAIN_KEUZE)
  volgorde = models.PositiveIntegerField(default=0)
  leeftijd = models.CharField(max_length =100, default = 8)
  interesses = models.ManyToManyField(Interesse)

  def publish(self):
    self.datum = timezone.now()
    self.save()

  def __str__(self):
    return self.naam
  
  class Meta:
    ordering = ['volgorde']
#// CONTACTFORMULIER#