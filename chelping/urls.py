from django.urls import path
from .views import *
from .views import index, C_Aanvraag
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('index.html/', index ),
    path('diensten.html/', diensten ),

    path('tarieven.html/', tarief ),
    #TRAININGEN
    path('trainingen/faalangst.html/', faalangst),
    path('trainingen/nederlands.html/', nederlands),
    path('trainingen/remedial.html/', rt),
    path('trainingen/leerleren.html/', leerleren),

    #FORMULIEREN
    path('contact.html/', C_Aanvraag),
    ]

