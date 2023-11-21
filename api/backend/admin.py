from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('cadastral_number', 'width', 'longitude', 'status')
    search_fields = ('cadastral_number',)
    list_filter = ('status',)


admin.site.register(Service, ServiceAdmin)
