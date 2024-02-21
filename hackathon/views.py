from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse

from .models import Hackathon

# Create your views here.
def get_hackathon_choices(request):
    cities_kenya_choices = Hackathon.CITIES_KENYA
    supported_ages_choices = Hackathon.SUPPORTED_AGES
    supported_years_choices = Hackathon.SUPPORTED_YEARS
    sex_choices = Hackathon.SEX_CHOICES
    participation = Hackathon.PARTICIPATION
    experience = Hackathon.EXPERIENCE
    hear_us = Hackathon.HEAR_US

    data = {
        "cities_kenya": cities_kenya_choices,
        "supported_ages": supported_ages_choices,
        "supported_years": supported_years_choices,
        "sex_choices": sex_choices,
        "participation": participation,
        "experience": experience,
        "hear_us": hear_us
    }

    return JsonResponse(data)