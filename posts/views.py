from django.shortcuts import render
from .models import Post
from .serializers import PostCreateSerializer, PostDetailSerializer
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if(self.action == 'create'):
            return PostCreateSerializer
        else: 
            return PostDetailSerializer
        
    queryset = Post.objects.all().order_by('-created_datetime')
