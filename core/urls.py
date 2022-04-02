
from django.urls import path, include
from .views import BlogDetailListAPIView, BlogListAPIView, CreateBlogAPIView

urlpatterns = [

    path('', BlogListAPIView.as_view(), name='blog'),
    path('create/', CreateBlogAPIView.as_view(), name='add_blog'),
    
    
    path('<str:slug>/', BlogDetailListAPIView.as_view(), name='blog_detail'),
    
]