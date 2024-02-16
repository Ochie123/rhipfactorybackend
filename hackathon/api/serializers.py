# serializers.py

from rest_framework import serializers
from hackathon.models import Stack, Healthcare, Hackathon, Primaryskill

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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Obfuscate sensitive information
        data['email'] = "********"
        data['number'] = "********"
        return data
    
class PrimaryskillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Primaryskill
        fields = '__all__'