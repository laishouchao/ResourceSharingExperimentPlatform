from django.contrib import admin
from .models import SystemSetting


# Register your models here.

@admin.register(SystemSetting)
class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'LogoFile', 'IPSetting', 'PortRangeStart', 'PortRangeStop',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
