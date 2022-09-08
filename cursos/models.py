from django.db import models

class Matematica(models.Model):
    fecha_de_inicio=models.CharField(max_length=50)
    profesor=models.CharField(max_length=50)
    cantidad_de_clases=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.fecha_de_inicio+ " del "+ self.profesor
    
class Lengua(models.Model):
    fecha_de_inicio=models.CharField(max_length=50)
    profesor=models.CharField(max_length=50)
    cantidad_de_clases=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.fecha_de_inicio+ " del "+ self.profesor

    
class Quimica(models.Model):
    fecha_de_inicio=models.CharField(max_length=50)
    profesor=models.CharField(max_length=50)
    cantidad_de_clases=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.fecha_de_inicio+ " del "+ self.profesor

    