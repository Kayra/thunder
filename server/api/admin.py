from django.contrib import admin
from .models import Routine, Exercise

admin.register(Routine, Exercise)(admin.ModelAdmin)
