from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('home.html', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signinup.html',views.signinupPage, name="Signinup"),
    path('event.html',views.eventlist, name="Event"),
]