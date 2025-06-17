from django.shortcuts import render
from .forms import Form_Co

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
  if request.method== "POST":
    print('op verzendknop_FT geklikt')
    co_form = Form_Co(request.POST) #info ophalen
    pass
  else:
    pass
    co_form = Form_Co()
  # // KLIK OP VERZENDEN
  print('formulier is ingediend > dankbericht verschijnt')
  return render(request, 'contact.html', {'co_form':  co_form}) # formulier blijft gevuld :)