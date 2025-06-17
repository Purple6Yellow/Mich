from django.contrib import admin
from .models import Contact


admin.site.site_header = "Chelping"
admin.site.register(Contact)