from django.contrib import admin

# Register your models here.
from .models import Bean, Review

admin.site.register(Bean)
admin.site.register(Review)
