from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):

 turnOff=serializers.CharField(allow_null=True,default=None,max_length=100)

 def create(self, validated_data: dict) -> Service:
        return Service.objects.create(**validated_data)


 class Meta:
        model = Service
        fields = ["id", "turnOn", "turnOff", "active"]


