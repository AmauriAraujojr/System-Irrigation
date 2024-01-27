from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from .models import Service
from .serializers import ServiceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ServiceView(ListCreateAPIView):
 authentication_classes=[JWTAuthentication]
 permission_classes=[IsAuthenticated]

 queryset= Service.objects.all()
 serializer_class= ServiceSerializer
 
 def perform_create(self, serializer):
  user=self.request.user
  return serializer.save(user=user)
 
class ServicesDetailView(RetrieveUpdateAPIView):
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAuthenticated]
  
  queryset=Service.objects.all()
  serializer_class= ServiceSerializer


  