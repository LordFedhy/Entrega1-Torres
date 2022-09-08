from cursos.views import buscar, insertar_matematica, insertar_lengua, insertar_quimica
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("buscar", buscar,name="buscar"),
    path("insertar_matematica", insertar_matematica),
    path("insertar_lengua", insertar_lengua),
    path("insertar_quimica",insertar_quimica)
]