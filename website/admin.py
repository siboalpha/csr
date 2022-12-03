from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(contactMessage)
class contactMessageAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone_number', 'email'