# views.py

from rest_framework import viewsets
from hackathon.models import Stack, Healthcare, Hackathon, Primaryskill
from hackathon.api.serializers import StackSerializer, HealthcareSerializer, HackathonSerializer, PrimaryskillSerializer

class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

class HealthcareViewSet(viewsets.ModelViewSet):
    queryset = Healthcare.objects.all()
    serializer_class = HealthcareSerializer

class HackathonViewSet(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class PrimaryskillViewSet(viewsets.ModelViewSet):
    queryset = Primaryskill.objects.all()
    serializer_class = PrimaryskillSerializer