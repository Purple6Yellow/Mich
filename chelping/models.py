from django.db import models
from django.utils import timezone
from PIL import Image


# CONTACTFORMULIER#
class Contact(models.Model):
  naam = models.CharField('naam', max_length=50,  blank=False, null = True)
  leeftijd = models.CharField(blank = False,
        choices=[
        ('basisschool', '6-8'),
        ('onderbouw', '9-12'),
        ('mavo', '13-14'),
         ('havo', '2011-2015'),])
  niveau = models.CharField(max_length=30,default = 'Onbekend',blank=False, null = True,
    choices=[
        ('basisschool', 'basis'),
        ('onderbouw', 'onderbouw'),
        ('mavo', 'mavo'),
         ('havo', 'havo'),
        ('vmbo', 'vmbo'),])
  email = models.EmailField('email',unique=False,   blank=False, null = True)
  telefoon = models.CharField('telefoon', max_length=30, blank = False, null = True)
  akkoord = models.BooleanField(default=False, null= False, blank = False)
  training = models.CharField(max_length=30,default = 'Onbekend',blank=False, null = True,
    choices=[
        ('basisschool', 'Faalangst'),
        ('onderbouw', 'Leer leren'),
        ('mavo', 'Remedial Teaching'),
         ('havo', 'Nederlands'),])
  volgorde = models.PositiveIntegerField(default=0)

  def publish(self):
    self.datum = timezone.now()
    self.save()

  def __str__(self):
    return self.naam
  
  class Meta:
    ordering = ['volgorde']
#// CONTACTFORMULIER#