from django.db import models
from django.utils import timezone


# CONTACTFORMULIER#

NIV_CHOICES= [
  ('0','basisschool'),
  ('1','vmbo'),
  ('2','havo'),
  ('3','vwo'),
]
LEEFTIJD_KEUZE = [('5','5'),  ('6','6'),  ('17','17'),]
TRAIN_KEUZE = [('RT','Remidial Teaching'),  ('LL','Leer Leren'),  ('NL', 'Nederlands'),('FA','Faalangst training')]

class Contact(models.Model):
  naam = models.CharField('naam', max_length=50,  blank=False, null = True)
  leeftijd = models.CharField(blank = False, max_length = 30, null = True,choices=LEEFTIJD_KEUZE)       
  niveau = models.CharField(max_length=30,blank=False, choices=NIV_CHOICES, default = 'onbekend')
  email = models.EmailField('email',unique=False,   blank=False, null = True)
  telefoon = models.CharField('telefoon', max_length=30, blank = False, null = True)
  akkoord = models.BooleanField(default=False, null= False, blank = False)
  training = models.CharField(max_length=30,default = 'Onbekend',blank=False, null = True, choices=TRAIN_KEUZE)
 
  volgorde = models.PositiveIntegerField(default=0)

  def publish(self):
    self.datum = timezone.now()
    self.save()

  def __str__(self):
    return self.naam
  
  class Meta:
    ordering = ['volgorde']
#// CONTACTFORMULIER#