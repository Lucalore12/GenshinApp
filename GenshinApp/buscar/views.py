from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Personajes
from .forms import CrearPersonajeForm,BusquedaForm,EliminarForm


# Create your views here.
def crearUsuario(request):
    if request.method=='GET':
        return render(request,'signup.html',{'form' : UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user= User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Usuario Ya Existe"})
        else:
            return render(request, 'signup.html', {"form": UserCreationForm, "errorPassword": "Las Contraseñas no Coinciden"})


def home(request):
    personajes = Personajes.objects.all()
    return render(request,'home.html',{'personajes':personajes})

@login_required 
def CrearPersonajes(request):
    if request.method == "GET":
        return render(request, 'create.html', {"form": CrearPersonajeForm})
    else:
        try:
            form = CrearPersonajeForm(request.POST,request.FILES)
            form.autor=request.user
            nuevo_personaje=form.save(commit=False)
            nuevo_personaje.autor=request.user
            nuevo_personaje.save()
            return redirect('home')
        except ValueError:
            return render(request, 'create.html', {"form": CrearPersonajeForm, "error": "Error Creando Personaje"})
        
@login_required
def PersonajesCreados(request):
    personajes = Personajes.objects.filter(autor=request.user)
    return render(request, 'personajes_creados.html', {"Personajes": personajes})

def BuscarPersonajes(request):
    if request.method=='GET':
        return render(request,'buscar.html',{"form":BusquedaForm})
    else:
        formulario = BusquedaForm(request.POST)
        if formulario.is_valid():
            busqueda = formulario.cleaned_data['busqueda']
            resultados = Personajes.objects.filter(nombre__iexact=busqueda)
            return render(request, 'buscar.html', {'form':BusquedaForm,'resultados': resultados})

def CerrarSession(request):
    logout(request)
    return redirect('home')

def IniciarSession(request):
    if request.method=='GET':
        return render(request,'login.html', {"form":AuthenticationForm })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'login.html', {"form":AuthenticationForm ,"error" : "El Usuario o Contraseña Son Incorrectos"})
        login(request,user)
        return redirect('home')

@login_required    
def Modificar(request,pk):
    personaje= get_object_or_404(Personajes,pk=pk)
    if request.method=='POST':
        form=CrearPersonajeForm(request.POST,instance=personaje)
        if form.is_valid(): 

            form.save()
            return redirect('home')
    else:
        form=CrearPersonajeForm(instance=personaje)
    return render(request,'modificar.html', {'form': form})
        
@login_required
def eliminar_Personaje(request, pk):
    objeto = Personajes.objects.get(pk=pk)
    form = EliminarForm(request.POST or None, initial={'id': objeto.id})

    if request.method == 'POST' and form.is_valid():
        objeto.delete()
        messages.success(request, 'Objeto eliminado correctamente.')
        return redirect('personajes_creados')  # Redirige a la lista de objetos

    return render(request, 'eliminar.html', {'form': form, 'objeto': objeto})

def ver_detalles(request,pk):
    personaje= get_object_or_404(Personajes,pk=pk)
    return render(request,'personaje.html',{'personaje':personaje})