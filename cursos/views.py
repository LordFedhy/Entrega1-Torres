from .models import Matematica, Quimica, Lengua
from django.shortcuts import render
from django.http import HttpResponse

def buscar(request):
    if request.method == "POST":
        profesor = request.POST["profesor"]
        if Matematica.objects.filter(profesor__contains=profesor):
            matematicas = Matematica.objects.filter(profesor__contains=profesor)
            return render(request,"buscar.html",{"matematicas":matematicas})
        elif Quimica.objects.filter(profesor__contains=profesor):
            quimicas = Quimica.objects.filter(profesor__contains=profesor)
            return render(request,"buscar.html",{"quimicas":quimicas})
        elif Lengua.objects.filter(profesor__contains=profesor):
            lenguas = Lengua.objects.filter(profesor__contains=profesor)
            return render(request,"buscar.html",{"lenguas":lenguas})
        else:    
            return HttpResponse("material no encontrado")
    return render(request,"buscar.html")

def insertar_matematica(request):
    if request.method == "POST":
        matematica = Matematica(fecha_de_inicio = request.POST["fecha_de_inicio"],profesor = request.POST["profesor"],cantidad_de_clases=request.POST["cantidad_de_clases"])
        matematica.save()
        return render(request,"insertar_matematica.html")
    return render(request,"insertar_matematica.html")

def insertar_lengua(request):
    if request.method == "POST":
        lengua = Lengua(fecha_de_inicio = request.POST["fecha_de_inicio"],profesor = request.POST["profesor"],cantidad_de_clases=request.POST["cantidad_de_clases"])
        lengua.save()
        return render(request,"insertar_lengua.html")
    return render(request,"insertar_lengua.html")

def insertar_quimica(request):
    if request.method == "POST":
        quimica = Quimica(fecha_de_inicio = request.POST["fecha_de_inicio"],profesor = request.POST["profesor"],cantidad_de_clases=request.POST["cantidad_de_clases"])
        quimica.save()
        return render(request,"insertar_quimica.html")
    return render(request,"insertar_quimica.html")
# Create your views here.