from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, CustomUserCreationFrom
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.

def indexView(request):
    try:
        connected_client = get_object_or_404(Client, user=request.user)
    except:
        return render(request, 'index.html')
    
    return render(request, 'index.html', {'client': connected_client})


def loginView(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            loginData = loginForm.cleaned_data
            user = authenticate(request, username=loginData['username'], password=loginData['password'])

            if user is not None:
                login(request, user)
                return redirect('index')

    else:
        loginForm = LoginForm()
        return render(request, 'login.html', {'form': loginForm})

def logoutView(request):
    logout(request)
    return redirect('index')
    
def registerView(request):
    if request.method == 'POST':
        registerForm = CustomUserCreationFrom(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.save()

            client = Client()
            client.user = user
            client.nom = user.last_name
            client.prenom = user.first_name
            client.email = user.email
            client.save()
            
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('index')

    registerForm = CustomUserCreationFrom()
    return render(request, 'register.html', {'form': registerForm})
    

def carListingView(request):
    all_cars = Voiture.objects.all()
    return render(request, 'carListing.html', {'cars': all_cars})

def reservationListingView(request):
    all_reservations = Reservation.objects.all()
    return render(request, 'reservationsListing.html', {'reservations': all_reservations})

