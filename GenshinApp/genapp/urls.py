"""
URL configuration for genapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from buscar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.crearUsuario,name='signup'),
    path('logout/',views.CerrarSession,name='logout'),
    path('login/',views.IniciarSession,name='login'),
    path('create/',views.CrearPersonajes,name='create'),
    path('buscar/',views.BuscarPersonajes,name='buscar'),
    path('personajes_creados/',views.PersonajesCreados,name='personajes_creados'),
    path('modificar/<int:pk>',views.Modificar,name='modificar'),
    path('eliminar/<int:pk>',views.eliminar_Personaje,name='eliminar'),
    path('personaje/<int:pk>',views.ver_detalles,name='personaje'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
