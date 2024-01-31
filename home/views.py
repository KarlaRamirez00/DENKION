from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.

def index_home(request):
    context={}
    return render (request, 'home/index.html', context)

def nosotros(request):
    context={}
    return render (request, 'home/nosotros.html', context)

def contacto(request):
    context={}
    return render (request, 'home/contacto.html', context)

def co_contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y envía el correo electrónico
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['tel']
            tipo_consulta = form.cleaned_data['tipo_con']
            consulta = form.cleaned_data['con']

            # Envía el correo electrónico
            asunto = f'Mensaje de contacto de {nombre}'
            mensaje_email = f'Correo de contacto: {correo}\nTeléfono: +56 9 {telefono}\nTipo de consulta: {tipo_consulta}\n\nMensaje:\n{consulta}'
            destinatario = [settings.CONTACT_EMAIL]  # Reemplaza con tu dirección de correo electrónico

            send_mail(asunto, mensaje_email, settings.DEFAULT_FROM_EMAIL, destinatario)

            return redirect('exito')  # Redirige a una página de éxito
    else:
        form = ContactForm()

    return render(request, 'contacto.html', {'form': form})