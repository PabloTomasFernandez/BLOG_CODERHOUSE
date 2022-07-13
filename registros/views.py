from django.shortcuts import render, redirect
from .forms import  UserEditForm, UserRegisterForm
from .models import *
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')
            #autentificacion de usuario
            user= authenticate(username=usuario, password=clave)
            if user is not None:
                login(request,user)
                response = redirect('Inicio')
                return response
        else:
            form=AuthenticationForm()
            return render(request, 'registros/login.html',{'form':form,'mensaje':'Usuario o contraseña incorecta'})
    else:
        form=AuthenticationForm()
        return render(request,'registros/login.html', {'form':form})

def registro_request(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            response = redirect('login')
            return response
        
    else:
        form=UserRegisterForm()
        
    return render(request,'registros/registro.html',{'form':form})

def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'BlogApp/inicio.html',{'usuario':usuario, 'mensaje':'Dato Cambiado exitosamente'})
    else:
        formulario=UserEditForm(instance=usuario) 
    return render(request, 'registros/editarPerfil.html',{'formulario':formulario, 'usuario':usuario.username})

