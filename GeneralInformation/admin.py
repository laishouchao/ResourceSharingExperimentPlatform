from django.contrib import admin
from GeneralInformation.models import CourseManagement, ClassManagement, ContainerManagement, ExperimentalReport

# Register your models here.
# 定义系统名称
admin.site.site_title = '虚拟化计算资源共享实验系统'
admin.site.site_header = '虚拟化计算资源共享实验系统'


@admin.register(CourseManagement)
class CourseManagementAdmin(admin.ModelAdmin):
    list_display = ['CourseName', 'CourseContent', 'CourseStartTime', 'CourseStopTime', 'TemplateOfExperimentReport']
    list_filter = ['CourseName']
    search_fields = ['CourseName', 'CourseContent']
    fields = ['CourseName', 'CourseContent', 'CourseStartTime', 'CourseStopTime', 'JoinUsers', 'Experiments',
              'TemplateOfExperimentReport']


@admin.register(ClassManagement)
class ClassManagementAdmin(admin.ModelAdmin):
    # 显示的字段
    list_display = ['Level', 'Major', 'Class', 'Others']
    # 可以直接在列表页修改的字段
    list_editable = ['Major', 'Class', 'Others']
    # 过滤器，以 Level 字段进行过滤
    list_filter = ['Level']
    # 搜索字段
    search_fields = ['Level', 'Major', 'Class', 'Others']


# 为User功能补充班级及成绩字段
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'User'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(ContainerManagement)
class ContainerManagementAdmin(admin.ModelAdmin):
    list_display = (
        'ContainerName', 'ContainerCourse', 'ContainerUser', 'ContainerImage', 'ContainerPorts', 'ContainerStartTime')
    search_fields = ['ContainerName', 'ContainerCourse', 'ContainerCourse']
    list_filter = ['ContainerUser', 'ContainerCourse', 'ContainerStartTime']
    fields = ['ContainerName', 'ContainerCourse', 'ContainerUser', 'ContainerImage', 'ContainerPorts',
              'ContainerStartTime']

    def has_add_permission(self, request):
        return False


@admin.register(ExperimentalReport)
class ExperimentalReportAdmin(admin.ModelAdmin):
    list_display = ['Course', 'User', 'ReportFile', 'UploadTime']
    list_filter = ['Course', 'User']
    search_fields = ['Course', 'User']
