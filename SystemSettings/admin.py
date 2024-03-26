from django.contrib import admin
from .models import SystemLogoSetting
# Register your models here.

@admin.register(SystemLogoSetting)
class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'LogoFile', )

    def has_add_permission(self, request):
        return False