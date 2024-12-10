from django.db import models

# Create your models here.
class Empleado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    salario = models.IntegerField()
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido