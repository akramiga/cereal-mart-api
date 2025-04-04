from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import UserSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can list users

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can view user details

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user).data,
            'tokens': serializer.data['tokens'],
            'message': 'User created successfully'
        }, status=status.HTTP_201_CREATED)
    