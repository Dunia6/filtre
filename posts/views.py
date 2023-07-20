from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# import Response
from rest_framework.response import Response
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
        
        if not preferences:
            """ Récupérer tous les posts si l'utilisateur n'a pas de préférences"""
            queryset = Post.objects.all()
          
            return queryset
        else:
            # Filtrer les posts en fonction des préférences de l'utilisateur
            queryset = Post.objects.filter(category__in = preferences)
            
            return queryset


class PostLikeView(generics.GenericAPIView):
    """ PostLikeView class """
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
        
        if not preferences:
            """ Récupérer tous les posts si l'utilisateur n'a pas de préférences"""
            queryset = Post.objects.all()
          
            return queryset
        else:
            # Filtrer les posts en fonction des préférences de l'utilisateur
            queryset = Post.objects.filter(category__in = preferences)
            
            return queryset
        
    
    def post(self, request, pk):
        """ Ajout et suppression d'un like à un post  """
        post = self.get_object()
        user = request.user
        
        if user in post.likes.all():
            post.post_unlike(user)
            post.likes_count -= 1
        else:
            post.post_like(user)
            post.likes_count += 1
        
        serializer = self.get_serializer(post)
        
        return Response(serializer.data)