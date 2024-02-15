from django.urls import path
from . import views

urlpatterns = [
    path('api/hackathon-choices/', views.get_hackathon_choices, name='get_hackathon_choices'),
]