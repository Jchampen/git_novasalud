from django.db import models

# Create your models here.
class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    documento = models.IntegerField()
    foto = models.ImageField()