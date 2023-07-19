from django.db import models
from django.contrib.auth.models import User
from posts.models import Category
# Create your models here.

class Profile(models.Model):
    """ Model de la class Profile """
    preferences = models.ManyToManyField(Category, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Retourne un texte représentant l'objet """
        return self.user.username
    