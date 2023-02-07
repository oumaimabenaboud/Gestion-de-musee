from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signinup/',views.signinupPage, name="signinup"),
    path('manifestation/',views.manifestation, name="manifestation"),
    path('conference/',views.conference, name="conference"),
    path('oeuvre/',views.oeuvre, name="oeuvre"),
    path('contact/',views.contact, name="contact"),
    path('logout/', views.logout, name = "logout"),
    path('reservation',views.reservation,name='reservation'),
]