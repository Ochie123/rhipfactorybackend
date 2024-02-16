# urls.py

from django.urls import path, include
from rest_framework import routers
from . import views
#from .views import StackViewSet, HealthcareViewSet, HackathonViewSet

router = routers.DefaultRouter()
router.register(r'stacks', views.StackViewSet)
router.register(r'healthcares', views.HealthcareViewSet)
router.register(r'hackathons', views.HackathonViewSet)
router.register(r'primaryskills', views.PrimaryskillViewSet)

app_name = 'hackathon'
urlpatterns = [
    path('', include(router.urls)),
]
