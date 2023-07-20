from django.urls import path
from .views import PostListView, PostLikeView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='list_post'),
    path('posts/<int:pk>/like/', PostLikeView.as_view(), name='like_post'),
]