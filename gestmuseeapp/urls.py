from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signinup/',views.signinupPage, name="signinup"),
    path('manifestation/',views.manifestation, name="manifestation"),
    path('contact/',views.contact, name="contact"),
]