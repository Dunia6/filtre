from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """ Model de la class Category """
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'
        ordering = ['-created_at']
    def __str__(self):
        """ Retourne un texte représentant l'objet """
        return self.name


class Post(models.Model):
    """ Model de la class Post """
    title = models.CharField(max_length=100,null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
    
    def __str__(self):
        """ Retourne un texte représentant l'objet """
        return self.title
    