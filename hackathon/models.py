from django.test import TestCase

# Create your tests here.
from datetime import timedelta, date
from django.utils import timezone
from django.conf import settings

from django.urls import reverse

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from ckeditor_uploader.fields import RichTextUploadingField 
# Create your models here.
 


class Stack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Healthcare(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Primaryskill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
     
class Hackathon(models.Model):
    CITIES_KENYA = (
        ("Nairobi", "Nairobi"),
        ("Mombasa", "Mombasa"),
        ("Kisumu", "Kisumu"),
        ("Nakuru", "Nakuru"),
        ("Eldoret", "Eldoret"),
        ("Thika", "Thika"),
        ("Malindi", "Malindi"),
        ("Kitale", "Kitale"),
        ("Garissa", "Garissa"),
        ("Kakamega", "Kakamega"),
        ("Kiambu", "Kiambu")
    )
    SUPPORTED_AGES = (
        ("<20s", "<20s"),
        ("20s", "20s"),
        ("30's", "30's"),
        ("40's", "40's"),
        ("50's", "50's"),
        (">60's", ">60's"),
    )

    SUPPORTED_YEARS = (
        ("Zero", "Zero"),
        ("1 - 2 Years", "1 - 2 Years"),
        ("3 - 5 Years", "3 - 5 Years"),
        ("More than 5 Years", "More than 5 Years"),
    )

    SEX_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("prefer not to say", "Prefer not to say"),
    )

    PARTICIPATION = (
        ("yes", "Yes"),
        ("no", "No"),
    )

    EXPERIENCE = (
        ("yes", "Yes"),
        ("no", "No"),
    )

    HEAR_US = (
        ("word of mouth", "Word of Mouth"),
        ("online advert", "Online Advert"),
        ("social media", "Social Media"),
        ("website", "Website"),
        ("other", "Other"),
    )
    cities_kenya = models.CharField(max_length=255, choices=CITIES_KENYA)
    supported_ages = models.CharField(max_length=255, choices=SUPPORTED_AGES)
    supported_years = models.CharField(max_length=255, choices=SUPPORTED_YEARS)
    sex_choices = models.CharField(max_length=255, choices=SEX_CHOICES)
    participation = models.CharField(max_length=255, choices=PARTICIPATION)
    experience = models.CharField(max_length=255, choices=EXPERIENCE)
    hear_us = models.CharField(max_length=255, choices=HEAR_US)

    linkedin = models.CharField(max_length=5000)
    overview = RichTextUploadingField(max_length=5000)
    other_problems = RichTextUploadingField(("description"), blank=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number = models.IntegerField(blank=True)
    software_stack = models.ManyToManyField(Stack)
    skill = models.ManyToManyField(Primaryskill)  
    healthcare_problem = models.ManyToManyField(Healthcare)   
    created = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class PageView(models.Model): 
    ##model class for tracking the pages that a customer views """
    class Meta:
        abstract = True
    
    date = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField()
    tracking_id = models.CharField(max_length=255, db_index=True)
    
