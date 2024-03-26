# Generated by Django 3.2.8 on 2023-01-13 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GeneralInformation', '0003_auto_20230111_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentalReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReportFile', models.FileField(blank=True, max_length=300, upload_to='static/Upload/ExperimentReport', verbose_name='实验报告')),
                ('UploadTime', models.DateTimeField(verbose_name='上传时间')),
                ('Course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GeneralInformation.coursemanagement', verbose_name='课程')),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '实验报告',
                'verbose_name_plural': '实验报告',
            },
        ),
    ]