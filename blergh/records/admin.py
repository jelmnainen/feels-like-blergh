from django.contrib import admin

from .models import Stomach, Edible, Feeding

class StomachAdmin(admin.ModelAdmin):
    exclude = ['user']

class FeedingAdmin(admin.ModelAdmin):
    exclude = ['user']

admin.site.register(Stomach, StomachAdmin)
admin.site.register(Edible)
admin.site.register(Feeding, FeedingAdmin)
