from rest_framework import serializers
from .models import Service
from datetime import datetime


class ServiceSerializer(serializers.ModelSerializer):

 turnOff=serializers.CharField(allow_null=True,default=None,max_length=100)

 def create(self, validated_data: dict) -> Service:
        return Service.objects.create(**validated_data)

 def update(self, instance:Service, validated_data:dict) -> Service:
       instance.active=False
       instance.turnOff=datetime.now()
       instance.save()
       return instance
 
 class Meta:
        model = Service
        fields = ["id", "turnOn", "turnOff", "active"]


