from django.shortcuts import redirect, render
from .forms import FormularioContactos
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContactos()

    if request.method=="POST":
        formulario_contacto=FormularioContactos(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            
            email=EmailMessage('Mensaje de App Django',"{} te escribe desde {}:\n\n{}".format(nombre,email,contenido),"",["....@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
    return render(request, "contactos/contactos.html", {"miFormulario":formulario_contacto})