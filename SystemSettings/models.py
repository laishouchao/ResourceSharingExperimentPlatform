from django.db import models

# Create your models here.
class SystemLogoSetting(models.Model):
    LogoFile = models.FileField(upload_to='static/', max_length=300, null=True, verbose_name="系统Logo图片",)

    def __str__(self):
        # 返回LogoFile的文件名作为字符串
        return self.LogoFile.name

    class Meta:
        verbose_name = "Logo管理"
        verbose_name_plural = "Logo管理"