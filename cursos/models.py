from django.db import models
class Matematica(models.Model):
    fecha_de_inicio=models.CharField(max_length=50)
    profesor=models.CharField(max_length=50)
    cantidad_de_clases=models.CharField(max_length=50)
    
class Lengua(models.Model):
    fecha_de_inicio=models.CharField(max_length=50)
    profesor=models.CharField(max_length=50)
    cantidad_de_clases=models.CharField(max_length=50)
    
class Quimica(models.Model):
    fecha_de_inicio=models.CharField(max_length=50)
    profesor=models.CharField(max_length=50)
    cantidad_de_clases=models.CharField(max_length=50)
    