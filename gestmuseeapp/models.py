from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.urls import reverse
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.
user = get_user_model()

class Abonnee(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    cni = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    carte_payement= models.CharField(max_length=16)
    type_abonnement = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    password = models.CharField(max_length=255)


class Event(models.Model):
    title = models.CharField(u'Nom de la Manifestation', help_text=u'Nom de la Manifestation',max_length=100)
    theme = models.CharField(u'Thème de la Manifestation',help_text=u'Thème de la Manifestation',max_length=30,blank=True, null=True)
    start_day = models.DateField(u'Date de début de la Manifestation', help_text=u'Date de début de la Manifestation')
    end_day = models.DateField(u'Date de fin de la Manifestation', help_text=u'Date de fin de la Manifestation')
    image = models.ImageField(upload_to='static/img/manifestations')
    notes = models.TextField(u'Résumé', help_text=u'Résumé', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Manifestations'
        verbose_name_plural = u'Manifestations'
    class EventAdmin(admin.ModelAdmin):
        list_display = ['title','theme','start_day', 'end_day', 'image', 'notes']

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
 
    def clean(self):
        if self.end_day <= self.start_day:
            raise ValidationError("La date du début de l'événement doit être antérieure à celle de la fin de l'événement")
