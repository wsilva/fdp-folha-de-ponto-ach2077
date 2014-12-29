from django.contrib import admin

# Register your models here.

from .models import Registro

class RegistroAdmin(admin.ModelAdmin):
    list_display=['user', 'registro', 'criado_em', 'alterado_em']
    class Meta:
        model = Registro

admin.site.register(Registro, RegistroAdmin)
