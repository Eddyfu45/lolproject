from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Champion(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    lore = models.CharField(max_length=2000)

    abilityNameQ = models.CharField(max_length=100)
    abilityDescriptionQ = models.CharField(max_length=100)

    abilityNameW = models.CharField(max_length=100)
    abilityDescriptionW = models.CharField(max_length=100)

    abilityNameE = models.CharField(max_length=100)
    abilityDescriptionE = models.CharField(max_length=100)

    abilityNameR = models.CharField(max_length=100)
    abilityDescriptionR = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
def __str__(self):
    return self.name