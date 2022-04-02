from unicodedata import category
from django.db import models
from autoslug import AutoSlugField

from users.models import UserProfile

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='category_name')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name
    
    
class Blog(models.Model):
    Profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    content = models.TextField()
    image = models.ImageField(upload_to="blogimg")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    