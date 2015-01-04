from django.contrib import admin

# Register your models here.

from .models import Timesheet

class TimesheetAdmin(admin.ModelAdmin):
    list_display=['user', 'registro', 'criado_em', 'alterado_em']
    class Meta:
        model = Timesheet

admin.site.register(Timesheet, TimesheetAdmin)
