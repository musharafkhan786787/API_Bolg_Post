from django.urls import path
from .views import BlogPostListCreateAPIView

urlpatterns = [
    path('posts/', BlogPostListCreateAPIView.as_view(), name='post-list-create'),
]
