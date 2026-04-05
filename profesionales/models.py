from django.db import models

# Create your models here.
class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    documento = models.IntegerField()
    foto = models.ImageField(upload_to='profesionales/fotos/', null=True, blank=True)

    def __str__(self):
        return self.nombre