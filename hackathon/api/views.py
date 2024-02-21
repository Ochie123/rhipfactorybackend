from rest_framework import viewsets
from .permissions import IsAuthenticatedOrReadOnlyForDelete
from hackathon.models import Stack, Healthcare, Hackathon, Primaryskill
from hackathon.api.serializers import StackSerializer, HealthcareSerializer, HackathonSerializer, PrimaryskillSerializer

class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForDelete]

class HealthcareViewSet(viewsets.ModelViewSet):
    queryset = Healthcare.objects.all()
    serializer_class = HealthcareSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForDelete]

class HackathonViewSet(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForDelete]

class PrimaryskillViewSet(viewsets.ModelViewSet):
    queryset = Primaryskill.objects.all()
    serializer_class = PrimaryskillSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForDelete]
