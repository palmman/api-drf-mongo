from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from .serializers import BlogSerializer
from .models import Blog
# Create your views here.

# class BlogFilter(filters.FilterSet):
#     class Meta:
#         model = Blog
#         fields = {
#             'name': ['icontains'],
#             'content': ['icontains'],
#         }
        


class BlogListAPIView(generics.ListAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('name', 'content')
    
    
class BlogDetailListAPIView(generics.RetrieveAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    
class CreateBlogAPIView(generics.CreateAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    
    
    
    

    