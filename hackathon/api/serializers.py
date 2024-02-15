# serializers.py

from rest_framework import serializers
from hackathon.models import Stack, Healthcare, Hackathon

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'

class HealthcareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healthcare
        fields = '__all__'

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'
