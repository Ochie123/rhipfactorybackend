from django.contrib import admin

# Register your models here.
# /products/admin.py
from copy import copy
from openpyxl import Workbook
from openpyxl.styles import Alignment, NamedStyle, builtins
from openpyxl.styles.numbers import FORMAT_NUMBER
#from openpyxl.writer.excel import save_virtual_workbook

from django.contrib import admin
from django import forms
from django.db import models
from django.http.response import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from ordered_model.admin import OrderedTabularInline, OrderedInlineModelAdminMixin

from .models import Healthcare, Hackathon, PageView, Stack, Primaryskill

admin.site.site_header = 'Hackathon Administration'
admin.site.site_header_color = "purple" 
admin.site.module_caption_color = "grey"
 
@admin.register(Healthcare)
class HealthcareAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Primaryskill)
class PrimaryskillAdmin(admin.ModelAdmin):
    list_display = ['name']



class StackInline(OrderedTabularInline):
    model = Stack
    extra = 0
   # fields = ("get_software_stack_preview", "software_stack", "order", "move_up_down_links")
   #readonly_fields = ("get_software_stack_preview", "order", "move_up_down_links")
    #ordering = ("order",)


@admin.register(Hackathon)
class HackathonAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    list_display = ["name",'email','number', "experience"]
    list_display_links = ["name", "email"]
    list_editable = ["experience"]
    list_filter = ['sex_choices', 'software_stack', 'experience', 'supported_ages', ]

    #actions = [export_xlsx]

    fieldsets = ((_("Product"), {"fields": ("name","email","linkedin","number","overview","sex_choices", "supported_ages","supported_years","skill","software_stack","healthcare_problem","other_problems","participation", 'experience', 'hear_us', )}),)
  #  prepopulated_fields = {"slug": ("name",)}
   # inlines = [ProductImageInline]



