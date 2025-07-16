from django.shortcuts import render
from .forms import Form_Co
######## mail verzenden #########
from django.core.mail import EmailMessage


##

###ALGEMEEN
def index(request):
  return render (request, 'index.html' )
def contact(request):
  return render (request, 'contact.html' )
def diensten(request):
  return render (request, 'diensten.html' )
def tarief(request):
  return render (request, 'tarieven.html' )
###TRAINIG
def faalangst(request):
  return render (request, 'trainingen/faalangst.html' )
def nederlands(request):
  return render (request, 'trainingen/nederlands.html' )
def leerleren(request):
  return render (request, 'trainingen/leerleren.html' )
def rt(request):
  return render (request, 'trainingen/remedial.html' )


###CONTACTFORMULIER
def C_Aanvraag(request):
  # INFORMATIE # 
  onderwerp = "Inschrijving voor een training"
  email_aanvrager = 'vikamper@hotmail.com'
  #// INFORMATIE # 
  submitted = False
  popup = False
  if request.method== "POST":
    print('op verzendknop_FT geklikt')
    co_form = Form_Co(request.POST) #info ophalen
    #FORM GOED INGEVULD #
    if co_form.is_valid():
      co_form.save() #opslaan in admin omgeving
      #VOORWAARDE AKKOORD #
      #// VOORWAARDE AKKOORD #
      #EMAIL VERZENDEN#
      email = EmailMessage(
        subject = onderwerp,
        body = co_form.contact_mail(),
        from_email = 'info@chelping.nl',
        to = ['vikamper@hotmail.com'],
        bcc= [''])
      email.send(fail_silently = False) # op True zetten bij productie 
      print("email verzonden")
      submitted = True
      print('formulier is ingediend > dankbericht verschijnt')
      #//EMAIL VERZENDEN#
    else:
      popup = True
      print('Formulier is niet volledig ingevuld')
      #//FORM GOED INGEVULD #
  else:
    co_form = Form_Co()
  # // KLIK OP VERZENDEN
  return render(request, 'contact.html', {'co_form':  co_form, 'submitted':submitted, 'popup':popup}) # formulier blijft gevuld :)