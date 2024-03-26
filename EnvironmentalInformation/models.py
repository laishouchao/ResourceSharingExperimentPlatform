from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User  # 导入系统用户信息模型


# Create your models here.

# 实验指导书
class Guidances(models.Model):
    GuidanceName = models.CharField(max_length=40, default='实验指导书名称', verbose_name="实验指导书名称", )
    GuidanceContent = RichTextField(verbose_name="实验指导书内容", )

    def __str__(self):
        return self.GuidanceName

    class Meta:
        verbose_name = "实验指导"
        verbose_name_plural = "实验指导书"


class Experiments(models.Model):
    ExperimentName = models.CharField(max_length=40, default='环境名称', verbose_name="环境名称", )
    ExperimentInformation = models.CharField(max_length=40, default='环境简介', verbose_name="环境简介", )
    ExperimentImage = models.CharField(max_length=100, default='实验环境Image', verbose_name="实验环境Image", )
    ExperimentPorts = models.CharField(max_length=30, default='实验环境服务端口信息，多个端口请使用空格分隔', verbose_name="实验环境映射端口", )
    ExperimentGuidance = models.ForeignKey(Guidances, on_delete=models.SET_NULL, null=True, default="",
                                           verbose_name='实验指导书')

    def __str__(self):
        return self.ExperimentName

    class Meta:
        verbose_name = "实验基础环境"
        verbose_name_plural = "实验基础环境"


# 启动后生成的容器管理
class ContainerManagement(models.Model):
    ContainerName = models.CharField(max_length=40, verbose_name="容器名称", )
    ContainerUser = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="启动容器的用户", )
    ContainerImage = models.ForeignKey(Experiments, on_delete=models.CASCADE, verbose_name="容器基于的Image", )
    ContainerPorts = models.CharField(max_length=30, verbose_name="容器端口映射", )
    ContainerStartTime = models.DateTimeField(verbose_name='容器启动时间')

    def __str__(self):
        return self.ContainerName

    class Meta:
        verbose_name = "实验容器管理"
        verbose_name_plural = "实验容器管理"
