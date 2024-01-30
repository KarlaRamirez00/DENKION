from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
@login_required
def crud_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes':clientes}
    print("estoy enviando datos")
    return render(request, "clientes/clientes_list.html", context)

@login_required
def clientes_ag(request):
    context={}

    if request.method == "POST":
        rut=request.POST["rut"]
        dv=request.POST["dv"]
        password=request.POST["password"]
        email=request.POST["email"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        fec_nac=request.POST["fec_nac"]
        tele=request.POST["tele"]
        region=request.POST["region"]
        ciudad=request.POST["ciudad"]
        comuna=request.POST["comuna"]
        dire=request.POST["dire"]

        cliente_manager= Cliente.objects

        cliente = cliente_manager.create_user(rut=rut, dv=dv,password=password, email=email, first_name=first_name, last_name=last_name,fec_nac=fec_nac, tele=tele, region=region, ciudad=ciudad, comuna=comuna, dire=dire)

        return redirect('clientes_add')
    else:
        context= {}
        return render(request, 'clientes/clientes_add.html', context)

@login_required  
def clientes_edit(request, pk):
    cliente = Cliente.objects.get(rut=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            if 'password' in form.changed_data:
                form.instance.password = make_password(form.cleaned_data['password'])
            form.save()
            print("guardado exitosamente!")
            return redirect('clientes_edit', pk=pk)
        else:
            print("El formulario no es válido")
            print(form.errors)
    else:
        form = ClienteForm(instance=cliente)
    context = {'cliente': cliente, 'form': form}
    return render(request, 'clientes/clientes_edit.html', context)

@login_required    
def clientes_del(request, pk):
    mensajes=[]
    errores=[]
    clientes = Cliente.objects.all()
    try:
        clientes = Cliente.objects.get(rut=pk)
        context={}
        if clientes:
            clientes.delete()
            mensajes.append("Perfecto! Datos eliminados")
            context = {'clientes':clientes, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'clientes/clientes_list.html', context)
        else:
            context={}
            return render(request, 'clientes/clientes_list.html', context)
    except:
        print("Lo sentimos! No existe tal cliente")
        clientes=Cliente.objects.all()
        mensaje="Lo sentimos! No existe tal cliente"
        context={'mensaje':mensaje, 'clientes':clientes}
        return render (request, 'clientes/clientes_list.html', context)

   
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user != None:
            login(request, user)
            
            if user.is_staff:
                return redirect('crud_clientes')
            else:
                return render(request, "home/index.html")
        else:
            return render (request, "home/index.html")
    return render (request, "clientes/clientes_list.html")        


