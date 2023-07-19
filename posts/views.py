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
        
        # recuperer l'utiliseur actuel
        user = self.request.user
        
        # recuperer le profile de l'utilisateur
        profile = user.profile
        
        # recuperations des preferences de l'utilisateur
        preferences = profile.preferences.all()
        
        # Filtrer les posts en fonction des preferences de l'utilisateur
        queryset = Post.objects.filter(category__in = preferences)
        
        return queryset