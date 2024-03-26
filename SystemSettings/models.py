from django.db import models

# Create your models here.
class SystemSetting(models.Model):
    LogoFile = models.FileField(upload_to='static/', max_length=300, null=True, verbose_name="系统Logo图片",)
    IPSetting = models.GenericIPAddressField(null=True, verbose_name='容器系统IP地址')
    PortRangeStart = models.IntegerField(verbose_name='生成容器端口开始')
    PortRangeStop = models.IntegerField(verbose_name='生成容器端口截至')

    def __str__(self):
        # 返回LogoFile的文件名作为字符串
        return self.LogoFile.name

    class Meta:
        verbose_name = "系统设置"
        verbose_name_plural = "系统设置"