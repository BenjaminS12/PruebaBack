from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'registro/signup.html', {
            'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
            password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado exitosamente!')
            except:
                return render(request, 'registro/signup.html', {
                     'form': UserCreationForm,
                     "error":'Este Usuario ya existe'
                 })
        return render(request, 'registro/signup.html', {
                     'form': UserCreationForm,
                     "error":'Las contraseñas no coinciden'
                 })
        
def signin(request):
    return render(request, 'registro/signin.html')