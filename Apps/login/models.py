from django.db import models

# Create your models here.
class Registro(models.Model):
    id = models.AutoField(primary_key=True) 
    nombreUsuario = models.CharField(max_length=20)
    correoElectronico = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nombreUsuario} - {self.correoElectronico}'

class Provee(models.Model): 
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.numero)
