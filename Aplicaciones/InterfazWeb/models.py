from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    ingreso = models.CharField(max_length=50)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.rut, self.nombre, self.email, self.password, self.ingreso)