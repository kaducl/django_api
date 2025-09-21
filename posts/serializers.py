from rest_framework import serializers
from .models import Post 

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id','username', 'created_datatime')

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ('username', 'title', 'content')