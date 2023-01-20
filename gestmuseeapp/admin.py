from django.contrib import admin
from .models import Abonnee
from .models import Event
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe

# Register your models here.

admin.site.register(Abonnee)

class EventAdmin(admin.ModelAdmin):
    list_display = ['title','theme','start_day', 'end_day', 'image', 'notes']
 
admin.site.register(Event, Event.EventAdmin)