from django.contrib import admin
from django.urls import path, include
from chelping.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include ('chelping.urls')),
]

