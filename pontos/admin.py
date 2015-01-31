from django.contrib import admin

# Register your models here.

from .models import SpotHit

class SpotHitAdmin(admin.ModelAdmin):
    list_display=['user', 'spothit_datetime', 'created_at', 'updated_at']
    class Meta:
        model = SpotHit

admin.site.register(SpotHit, SpotHitAdmin)
