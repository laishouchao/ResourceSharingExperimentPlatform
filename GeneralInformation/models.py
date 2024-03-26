from django.db import models
from django.contrib.auth.models import User
from EnvironmentalInformation.models import Experiments


# Create your models here.

# 班级管理
class ClassManagement(models.Model):
    Level = models.CharField(max_length=40, null=True, verbose_name="年级", )
    Major = models.CharField(max_length=40, null=True, verbose_name="专业", )
    Class = models.CharField(max_length=40, null=True, verbose_name="班号", )
    Others = models.CharField(max_length=40, null=True, verbose_name="备注", )

    def __str__(self):
        return str(self.Level) + str(self.Major) + str(self.Class) + str(self.Others)

    class Meta:
        verbose_name = "班级管理"
        verbose_name_plural = "班级管理"


from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Class = models.ForeignKey(ClassManagement, on_delete=models.SET_NULL, null=True, verbose_name="所属班级")
    Score = models.PositiveIntegerField(verbose_name='成绩')

    def __str__(self):
        return self.User.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"


# 课时管理
class CourseManagement(models.Model):
    CourseName = models.CharField(max_length=40, default='课时名称', verbose_name="课时名称", )
    CourseContent = models.CharField(max_length=50, null=True, verbose_name="课程要求", )
    CourseStartTime = models.DateTimeField(verbose_name="课程开始时间", )
    CourseStopTime = models.DateTimeField(verbose_name="课程结束时间", )
    JoinUsers = models.ManyToManyField(User, verbose_name="参加课程的用户", )  # 参赛选手多选
    Experiments = models.ManyToManyField(Experiments, verbose_name="课时包含的实验环境", )  # 实验多选
    TemplateOfExperimentReport = models.FileField(upload_to='static/Upload/TemplateOfExperimentReport', max_length=300,
                                                  blank=True,
                                                  verbose_name="实验报告模板文件", )  # 实验报告模板文件

    def __str__(self):
        return self.CourseName

    class Meta:
        verbose_name = "课时管理"
        verbose_name_plural = "课时管理"


# 启动后生成的容器管理
class ContainerManagement(models.Model):
    ContainerName = models.CharField(max_length=40, null=True, verbose_name="容器名称", )
    ContainerCode = models.CharField(max_length=40, null=True, verbose_name="容器Hash编码", )
    ContainerCourse = models.ForeignKey(CourseManagement, on_delete=models.CASCADE, verbose_name="容器归属课程", )
    ContainerUser = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="启动容器的用户", )
    ContainerImage = models.ForeignKey(Experiments, on_delete=models.CASCADE, verbose_name="容器基于的Image", )
    ContainerPorts = models.CharField(max_length=30, verbose_name="容器端口映射", )
    ContainerStartTime = models.DateTimeField(verbose_name='容器启动时间')

    def __str__(self):
        return self.ContainerName

    class Meta:
        verbose_name = "实验容器"
        verbose_name_plural = "实验容器"


# 实验报告
class ExperimentalReport(models.Model):
    Course = models.ForeignKey(CourseManagement, on_delete=models.SET_NULL, null=True, verbose_name='课程')
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='用户')
    ReportFile = models.FileField(upload_to='static/Upload/ExperimentReport', max_length=300,
                                  blank=True,
                                  verbose_name="实验报告", )  # 实验报告模板文件
    UploadTime = models.DateTimeField(verbose_name='上传时间')

    def __str__(self):
        return self.Course.CourseName

    class Meta:
        verbose_name = "实验报告"
        verbose_name_plural = "实验报告"
