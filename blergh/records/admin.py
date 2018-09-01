from django.contrib import admin

from .models import Stomach

class StomachAdmin(admin.ModelAdmin):
    exclude = ['user']

admin.site.register(Stomach, StomachAdmin)
