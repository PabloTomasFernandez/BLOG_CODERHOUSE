from attr import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from matplotlib import image
from traitlets import default
from .models import *
from django.forms import ModelForm

choices=Categoria.objects.all().values_list('name')
choice_list=[]
for item in choices:
    choice_list.append(item)


class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields=('titulo','subtitulo','categoria','autor','categoria','content','snippet')
        widgets ={
            'titulo': forms.TextInput(),
            'subtitulo':forms.TextInput(),
            'categoria':forms.Select(choices=choices),
            'autor': forms.Select(),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(),
        }
        
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

class PostForm(ModelForm):
    class Meta:
        model=Comment
        fields=('name','curpo')
        widgets ={
            'name': forms.TextInput(),
            'curpo':forms.Textarea(),
        }