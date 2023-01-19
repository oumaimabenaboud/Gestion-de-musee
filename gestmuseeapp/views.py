from django.shortcuts import redirect,render
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages, auth
from gestmuseeapp.models import abonne
from .models import Event
# Create your views here.
from django.http import HttpResponse

#home page
def home(request):
    return render(request, 'home.html',{})

def eventlist(request):
    events = Event.objects
    return render(request, 'Eventlist.html',{'events':events})


#signup page
def signinupPage(request):
    if request.method=='POST' and 'btnform2' in request.POST: 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']

        if password1 == password2 :
            if User.objects.filter(email=email).exists():
                messages.warning(request,'Email taken')
                return redirect('signinup/')
            else:
                myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
                myuser.save()
                # user_model = User.objects.get(username=email)
                # new_abonne = abonne.objects.create(user=user,id_user=user.id)
                # new_abonne.save()
                messages.success(request, "Votre compte est crée .")
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
