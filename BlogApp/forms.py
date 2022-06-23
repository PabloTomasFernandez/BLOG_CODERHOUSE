from attr import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from traitlets import default
from .models import *
from django.forms import ModelForm

class BlogForm(forms.Form):
    titulo=forms.CharField(max_length=50)
    subtitulo=forms.CharField(max_length=50)
    autor=forms.CharField(max_length=50)
    categoria=forms.CharField(max_length=50)
    content=forms.Textarea()
    image=forms.ImageField()
    

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        #"" hace vacia todo las caracteristicas que teine que tener asi no aparece un chorizo
        help_texts={k:''for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(required=True)
    password1=forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput, required=False)
    password2=forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput, required=False)
    last_name=forms.CharField(label='Modificar Apellido')
    first_name=forms.CharField(label='Modificar Nombre')
    class Meta:
        model=User
        fields=['email','last_name','first_name', 'password1','password2']
        #"" hace vacia todo las caracteristicas que teine que tener asi no aparece un chorizo
        help_texts={k:''for k in fields}
