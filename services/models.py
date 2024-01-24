from django.db import models
from users.models import User

class Service(models.Model):
   
   turnOn = models.DateTimeField(auto_now_add=True)
   turnOff= models.CharField(null=True,max_length=100)
   active= models.BooleanField(default=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services")

   