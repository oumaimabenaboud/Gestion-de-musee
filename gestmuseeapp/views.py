from django.shortcuts import redirect,render
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages, auth
from .models import Abonnee
from datetime import datetime, timedelta
from .models import Event
from datetime import date
# Create your views here.
from django.http import HttpResponse

#home page
def home(request):
    events = Event.objects
    # events = Event.objects.filter(start_day__gte=date.today())
    return render(request, 'home.html',{'events': events})

def eventlist(request):
    events = Event.objects
    return render(request, 'event.html',{'events':events})


#signup page
def signinupPage(request):
    if request.method=='POST' and 'btnform2' in request.POST: 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        type_abonnement = request.POST['type_abonnement']

        if password1 == password2 :
            if User.objects.filter(email=email).exists():
                messages.warning(request,'Email taken')
                return redirect('signinup/')
            else:
                # myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
                # myuser.save()
                # user_model = User.objects.get(username=email)
                # new_abonne = abonne.objects.create(user=user,id_user=user.id)
                # new_abonne.save()
                abonnee = Abonnee.objects.create(prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement, date_start=datetime.now(), date_end=datetime.now() + timedelta(days=365), password=password1)
                abonnee.save()
                messages.success(request, "Votre compte est crée .")
                # abonne = abonne.objects.create(prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement, date_start=datetime.now(), date_end=datetime.now() + timedelta(days=365), password=password1)
                # abonne.save()
                # messages.success(request, "Votre compte est crée .")
                return redirect('home.html')
        else:
            messages.info(request,'password not matching')
            return redirect('signinup/')
    if request.method== 'POST' and 'btnform1' in request.POST:
        email = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home.html')
        else :
            messages.error(request,"Password missmatchs")
            return redirect('signinup')
    else: 
        return render(request, 'signinup.html')
