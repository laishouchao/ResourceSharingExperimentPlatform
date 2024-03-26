from django.db import models
from django.contrib.auth.models import User
import EnvironmentalInformation.models


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
    Experiments = models.ManyToManyField(EnvironmentalInformation.models.Experiments, verbose_name="课时包含的实验环境", )  # 实验多选
    TemplateOfExperimentReport = models.FileField(upload_to='static/Upload/TemplateOfExperimentReport', max_length=300,
                                                  blank=True,
                                                  verbose_name="实验报告模板文件", )  # 实验报告模板文件

    def __str__(self):
        return self.CourseName

    class Meta:
        verbose_name = "课时管理"
        verbose_name_plural = "课时管理"

# 实验报告

# 课程排名
