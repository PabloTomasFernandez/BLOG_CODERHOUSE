from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy, reverse
from .forms import  PostForm, UserEditForm, UserRegisterForm
from .models import *
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
class Inicio(ListView):
    model=Blog
    template_name= "BlogApp/inicio.html"
    cats=Categoria.objects.all()
    def get_context_data(self, *args, **kwargs):
        cat_menu=Categoria.objects.all()
        context=super(Inicio,self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        return context



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

class postCreacion(CreateView):
    model=Comment
    form_class= PostForm
    template_name= "BlogApp/comentarios.html"
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url= reverse_lazy('Inicio')

class categoriaCreacion(CreateView):
    model=Categoria
    template_name='BlogApp/categoria_creacion.html'
    fields='__all__'
#CRUD leer

class blogLista(ListView):
    model=Blog
    template_name= "BlogApp/blog_lista.html"
    orden=['-id']

class blogDetalle(DetailView):
    model=Blog
    template_name= "BlogApp/blog_detalle.html"
    def get_context_data(self, *args, **kwargs):
        cat_menu=Categoria.objects.all()
        
        stuff= get_object_or_404(Blog, id=self.kwargs['pk'])
        total_like= stuff.total_like()
        liked=False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked=True
        context=super(blogDetalle,self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        context['total_like']=total_like
        context['liked']=liked
        return context

def CategoriaVista(request, cats):
    categoria_blog=Blog.objects.filter(categoria=cats.replace('-',' '))
    return render(request, 'inicio.html', {'cats':cats.title().replace('-',' '), 'categoria_blog':categoria_blog})
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


def LikeView(request,pk):
    blog=get_object_or_404(Blog, id=request.POST.get('blog_id'))
    like=False
    if blog.like.filter(id=request.user.id).exists():
        blog.like.remove(request.user)
        like=False
    else:
        blog.like.add(request.user)
        like=True
    return HttpResponseRedirect(reverse('blog_detalle', args=[str(pk)]))