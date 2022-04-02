from django.shortcuts import render
from rest_framework import generics

from .models import Account, UserProfile

from .serializers import CreateAccountSerializer, ProfileSerializer

# Create your views here.

class CreateAccountAPIView(generics.CreateAPIView):
    
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer
    
class ProfileAPIView(generics.RetrieveAPIView):
    
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'
    


