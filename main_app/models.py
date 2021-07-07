from django.db import models
from django.contrib.auth.models import User
from django.forms.models import ModelForm


# Create your models here.

class Champion(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    lore = models.CharField(max_length=2000)

    abilityNameQ = models.CharField(max_length=100)
    abilityDescriptionQ = models.CharField(max_length=500)

    abilityNameW = models.CharField(max_length=100)
    abilityDescriptionW = models.CharField(max_length=500)

    abilityNameE = models.CharField(max_length=100)
    abilityDescriptionE = models.CharField(max_length=500)

    abilityNameR = models.CharField(max_length=100)
    abilityDescriptionR = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.CharField(max_length=2000)
    user = models.CharField(max_length=100)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    champion = models.PositiveIntegerField()
    # champion = models.ForeignKey(Champion, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    champion = models.OneToOneField(Champion, on_delete=models.CASCADE)