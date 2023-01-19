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
class abonne(models.Model):
    username = models.ForeignKey(user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    type = models.IntegerField()
    
    def __str__(self):
        return self.user.username

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
    # def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
    #     overlap = False
    #     if new_start == fixed_end or new_end == fixed_start:    #edge case
    #         overlap = False
    #     elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
    #         overlap = True
    #     elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
    #         overlap = True
 
    #     return overlap
 
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
 
    def clean(self):
        if self.end_day <= self.start_day:
            raise ValidationError("La date du début de l'événement doit être antérieure à celle de la fin de l'événement")
 
        # events = Event.objects.filter(day=self.day)
        # if events.exists():
        #     for event in events:
        #         if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
        #             raise ValidationError(
        #                 'There is an overlap with another event: ' + str(event.day) + ', ' + str(
        #                     event.start_time) + '-' + str(event.end_time))

# class Event(models.Model):
#     day = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     notes = models.TextField()

#     class Meta:
#         ordering = ['day']

#     class EventAdmin(admin.ModelAdmin):
#         list_display = ['day', 'start_time', 'end_time', 'notes']