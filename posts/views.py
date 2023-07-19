from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PostListView(generics.ListAPIView):
    """ PostListView class """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """ Returns a list of posts based on the user's preferences."""
        
        # recupérer l'utiliseur actuel
        user = self.request.user
        
        # recupérer le profile de l'utilisateur
        profile = user.profile
        
        # recupérer les préférences de l'utilisateur contenues dans le profile
        preferences = profile.preferences.all()
        
        # Filtrer les posts en fonction des préférences de l'utilisateur
        queryset = Post.objects.filter(category__in = preferences)
        
        return queryset