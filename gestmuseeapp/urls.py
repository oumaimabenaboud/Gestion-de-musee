from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signinup/',views.signinupPage, name="Signinup"),
    path('Eventlist/',views.eventlist, name="Event"),
]