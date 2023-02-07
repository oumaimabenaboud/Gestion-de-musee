from django.shortcuts import redirect,render
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages, auth
from .models import Abonnee
from datetime import datetime, timedelta
from .models import Event, Conference, Oeuvre, Reservation
from datetime import date
from allauth.account.models import EmailAddress
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#home page
def home(request):
    events = Event.objects
    abonnees = Abonnee.objects.all()
    context = {'events': events, 'abonnees': abonnees}
    return render(request, 'home.html',context)

def manifestation(request):
    events = Event.objects
    return render(request, 'manifestation.html',{'events':events})

def conference(request):
    conferences = Conference.objects
    return render(request, 'conference.html',{'conferences':conferences})
def oeuvre(request):
    oeuvres = Oeuvre.objects
    return render(request, 'oeuvre.html',{'oeuvres':oeuvres})

def contact(request):
    return render(request, 'contact.html',{})

def reservation (request):
    if request.method=='POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_str = request.POST['date']
        heure = request.POST['heure']
        nbr_pers = request.POST['nbr']
        selected_option = request.POST.get('choice')
        if selected_option == 'yes':
            guided = True
        else:
            guided = False
        print(guided)
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        if (date<datetime.now().date()):
            messages.error(request, "The date you entered has already passed. Please enter a valid date.")
            return redirect('home')
        else : 
            reservation = Reservation.objects.create(prenom=first_name, nom=last_name,date=date,heure=heure, nbr_pers=nbr_pers,guidee=guided)
            reservation.save()
            messages.success(request, "Your reservation was successful.")
            return redirect('home')

def logout (request):
    auth.logout(request)
    return redirect('home')


#signup page
def signinupPage(request):
    if request.method=='POST' and 'btnform2' in request.POST: 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        type_abonnement = request.POST['type_abonnement']
        type_abonne= request.POST['type_abonne']
        cni = request.POST['cni']
        carte_payement= request.POST['carte_payement']

        if password1 == password2 :
            if Abonnee.objects.filter(email=email).exists():
                messages.warning(request,'Email taken')
                return redirect('signinup')
            else:
                if type_abonnement == "Mensuel":
                    abonnee = Abonnee.objects.create(prenom=first_name, nom=last_name, email=email, cni=cni,carte_payement=carte_payement, type_abonne=type_abonne,type_abonnement =type_abonnement, date_start=datetime.now(), date_end=datetime.now() + timedelta(days=30), password=password1)
                    abonnee.save()
                    myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
                    myuser.save()
                    messages.success(request, "Votre compte a été créé.")

                elif type_abonnement == "Trimestriel":
                    abonnee = Abonnee.objects.create(prenom=first_name, nom=last_name, email=email, cni=cni,carte_payement=carte_payement, type_abonne=type_abonne, type_abonnement =type_abonnement,date_start=datetime.now(), date_end=datetime.now() + timedelta(days=90), password=password1)
                    abonnee.save()
                    myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
                    myuser.save()
                    messages.success(request, "Votre compte a été créé.")

                elif type_abonnement == "Semestriel":
                    abonnee = Abonnee.objects.create(prenom=first_name, nom=last_name, email=email, cni=cni,carte_payement=carte_payement, type_abonne=type_abonne, type_abonnement =type_abonnement, date_start=datetime.now(), date_end=datetime.now() + timedelta(days=183), password=password1)
                    abonnee.save()
                    myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
                    myuser.save()
                    messages.success(request, "Votre compte a été créé.")
                elif type_abonnement == "Annuel":
                    abonnee = Abonnee.objects.create(prenom=first_name, nom=last_name, email=email, cni=cni,carte_payement=carte_payement, type_abonne=type_abonne, type_abonnement =type_abonnement, date_start=datetime.now(), date_end=datetime.now() + timedelta(days=365), password=password1)
                    abonnee.save()
                    myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
                    myuser.save()
                    messages.success(request, "Votre compte a été créé.")

                return redirect('signinup')
        else:
            messages.info(request,'password not matching')
            return redirect('signinup')
    if request.method== 'POST' and 'btnform1' in request.POST:
        email = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Vous êtes connecté.")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('signinup')
    else: 
        return render(request, 'signinup.html')
