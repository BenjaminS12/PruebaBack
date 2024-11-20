from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def index(request):
    return render(request, 'index.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'registro/signup.html', {
            'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],password=request.POST
                    ['password1'])
                user.save()
                login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'registro/signup.html', {
                    'form': UserCreationForm,
                    "error":'Este usuario ya existe'
                })
        
        return render(request, 'registro/signup.html', {
            'form': UserCreationForm,
            "error":'Las contraseñas no coinciden'
        })
        
def signin(request):
    if request.method == 'GET':
        return render(request, 'templates/registro/signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'templates/registro/signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('index')
        