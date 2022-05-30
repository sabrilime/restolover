from django.db import models
from django.contrib.auth.models import User

class Specialite(models.Model):
    nom = models.CharField(max_length=100)

class Resto(models.Model):
    nom = models.CharField(max_length=32)
    adresse = models.CharField(max_length=120)
    code_postal = models.IntegerField()
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    halal = models.BooleanField(default = False)
    instagram = models.CharField(max_length=120, null=True, blank=True)
    tripadvisor = models.CharField(max_length=120, null=True, blank=True)
    specialites = models.ManyToManyField('Specialite', related_name='restos', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)