from django.shortcuts import render
from .forms import Form_Co
######## mail verzenden #########
import smtplib
from email.mime.text import MIMEText


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
  smtp_server = 'smtp.gmail.com'
  smtp_port = 587
  email_beheerder = 'code.magenta.2025@gmail.com'
  app_password = 'nety dhmf zwev szuj' #naam app wachtwoord: wachtlijst
  onderwerp = "Inschrijving voor een training"
  bericht = ""
  email_aanvrager = 'vikamper@hotmail.com'
  email_ontvanger = "vikamper@hotmail.com"
  #// INFORMATIE # 
  submitted = False
  if request.method== "POST":
    print('op verzendknop_FT geklikt')
    co_form = Form_Co(request.POST) #info ophalen
    #FORM GOED INGEVULD #
    if co_form.is_valid():
      co_form.save() #opslaan in admin omgeving
      #VOORWAARDE AKKOORD #
      #// VOORWAARDE AKKOORD #
      #EMAIL VERZENDEN#
      bericht = co_form.contact_mail()
      msg = MIMEText(bericht)
      msg['Subject'] = onderwerp
      msg['From'] = email_aanvrager
      msg['To'] = email_ontvanger
      with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() #TLS  gebruiken
        server.login(email_beheerder, app_password)
        server.sendmail(email_aanvrager, email_ontvanger, msg.as_string())
        print("email verzonden")
        submitted = True
        print('formulier is ingediend > dankbericht verschijnt')
      #//EMAIL VERZENDEN#
      pass
    else:
      pass
      #FORM GOED INGEVULD #
  else:
    pass
    co_form = Form_Co()
  # // KLIK OP VERZENDEN
  return render(request, 'contact.html', {'co_form':  co_form, 'submitted':submitted}) # formulier blijft gevuld :)