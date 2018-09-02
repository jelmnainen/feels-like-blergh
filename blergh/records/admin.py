from django.contrib import admin

from .models import Stomach, Edible

class StomachAdmin(admin.ModelAdmin):
    exclude = ['user']

admin.site.register(Stomach, StomachAdmin)
admin.site.register(Edible)
