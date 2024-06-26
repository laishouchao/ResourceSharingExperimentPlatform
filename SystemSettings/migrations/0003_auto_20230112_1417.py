# Generated by Django 3.2.8 on 2023-01-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemSettings', '0002_auto_20230112_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemsetting',
            old_name='IPRangeStart',
            new_name='PortRangeStart',
        ),
        migrations.RenameField(
            model_name='systemsetting',
            old_name='IPRangeStop',
            new_name='PortRangeStop',
        ),
        migrations.AddField(
            model_name='systemsetting',
            name='IPSetting',
            field=models.GenericIPAddressField(null=True, verbose_name='容器系统IP地址'),
        ),
    ]
