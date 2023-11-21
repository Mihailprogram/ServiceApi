from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('cadastral_number', 'width', 'longitude')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('width', 'longitude', 'status',)