from django.apps import AppConfig


class SystemsettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SystemSettings'

    verbose_name = '系统设置'
    verbose_name_plural = '系统设置'
