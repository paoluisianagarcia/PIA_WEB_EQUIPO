from django.db import models

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nombre
