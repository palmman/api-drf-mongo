from django.urls import path, include
from .views import CreateAccountAPIView, ProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('register/', CreateAccountAPIView.as_view(), name='name'),
    path('profile/<str:slug>', ProfileAPIView.as_view(), name='profile'),

    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
    
