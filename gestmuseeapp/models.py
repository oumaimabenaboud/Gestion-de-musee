from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.

class Abonnee(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    cni = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    carte_payement= models.CharField(max_length=16)
    type_abonnement = models.CharField(max_length=255)
    type_abonne = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    password = models.CharField(max_length=255)
    
class Artist(models.Model):
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    date_deces = models.DateField(blank=True, null=True)
    nationalite = models.CharField(max_length=255)


class Oeuvre(models.Model):
    titre = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    type_oeuvre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/oeuvres')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    type_assurance = models.CharField(max_length=255)

class Salle(models.Model):
    nom = models.CharField(max_length=50)
    capacite = models.IntegerField()
    est_valable = models.BooleanField()

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


class Conference(models.Model):
    titre = models.CharField(max_length=100)
    theme = models.CharField(max_length=50,blank=True, null=True)
    Conferencier = models.CharField(max_length=100)
    date_debut = models.DateField()
    duree = models.IntegerField(u'Durée de la conférence', help_text=u'Durée en minutes')
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/conference')
    notes = models.TextField(blank=True, null=True)

class Personel(models.Model):
    nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def check_availability(self, date):
        schedule = Schedule.objects.filter(personel=self, date=date)
        if schedule.exists():
            return False
        return True


class Schedule(models.Model):
    personel = models.ForeignKey(Personel, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()