from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from .forms import  UserEditForm, UserRegisterForm
from .models import *
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required

# Create your views here.
class Inicio(ListView):
    model=Blog
    template_name= "BlogApp/inicio.html"



def busquedaCategoriaBlog(request):
    return render(request, 'BlogApp/buscarCategoriaBlog.html')
def buscarCategoriaBlog(request):
    if request.GET['categoria']:
        categoria = request.GET['categoria']
        blogs = Blog.objects.filter(categoria = categoria)
        return render(request, 'BlogApp/resultadosCategoriaBlog.html', {'blogs': blogs, 'categoria': categoria})
    else:
        respuesta = "No hay blog sobre el tema"
    return HttpResponse(respuesta)

def buscarBlog(request):
    if request.GET['titulo']:
        busqueda = request.GET['titulo']
        blog = Blog.objects.filter(busqueda = busqueda)
        return render(request, 'BlogApp/resultadosBusquedaBlog.html', {'blog': blog, 'busqueda': busqueda})
    elif request.GET['autor']:
        busqueda = request.GET['autor']
        blog = Blog.objects.filter(busqueda = busqueda)
        return render(request, 'BlogApp/resultadosBusquedaBlog.html', {'blog': blog, 'busqueda': busqueda})
    elif request.GET['create']:
        busqueda = request.GET['create']
        blog = Blog.objects.filter(busqueda = busqueda)
        return render(request, 'BlogApp/resultadosBusquedaBlog.html', {'blog': blog, 'busqueda': busqueda})
    elif request.GET['categoria']:
        busqueda = request.GET['categoria']
        blog = Blog.objects.filter(busqueda = busqueda)
        return render(request, 'BlogApp/resultadosBusquedaBlog.html', {'blog': blog, 'busqueda': busqueda})
    else:
        respuesta = "No se ha encontrado busqueda"
    return render(request, 'BlogApp/resultadosBusquedaBlog.html', {'respuesta': respuesta})


#CRUD creacion

class blogCreacion(CreateView):
    model=Blog
    template_name= "BlogApp/blog_creacion.html"
    fields='__all__'

#CRUD leer

class blogLista(ListView):
    model=Blog
    template_name= "BlogApp/blog_lista.html"
    orden=['-id']

class blogDetalle(DetailView):
    model=Blog
    template_name= "BlogApp/blog_detalle.html"

#CRUD update

class blogActualizar(LoginRequiredMixin, UpdateView):
    model=Blog
    template_name= "BlogApp/blog_form.html"
    fields='__all__'

#CRUD delete
class blogEliminar(LoginRequiredMixin, DeleteView):
    model=Blog
    template_name= "BlogApp/blog_confirm_delete.html"
    success_url= reverse_lazy('Inicio')

#Inicio Seccion

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
                return render(request, 'BlogApp/inicio.html',{'mensaje':f'Bienvenido {usuario}'})
        else:
            return render(request, 'BlogApp/inicio.html',{'mensaje':'Usuario o contraseña incorecta'})
    else:
        form=AuthenticationForm()
        return render(request,'BlogApp/login.html', {'form':form})

def registro_request(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            return render(request,'BlogApp/inicio.html')
        
    else:
        form=UserRegisterForm()
        
    return render(request,'BlogApp/registro.html',{'form':form})

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
    return render(request, 'BlogApp/editarPerfil.html',{'formulario':formulario, 'usuario':usuario.username})