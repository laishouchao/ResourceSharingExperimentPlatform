from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Experiments, Guidances, ContainerManagement
from EnvironmentalInformation.forms import GuidancesAdminForm   # 导入自定义富文本编辑器CKEditor的表单


# Register your models here.
@admin.register(Experiments)
class ExperimentsAdmin(admin.ModelAdmin):
    list_display = ['ExperimentName', 'ExperimentInformation', 'ExperimentImage', 'ExperimentPorts',
                    'ExperimentGuidance']
    list_filter = ['ExperimentName']
    search_fields = ['ExperimentName', 'ExperimentInformation']
    fields = ['ExperimentName', 'ExperimentInformation', 'ExperimentImage', 'ExperimentPorts', 'ExperimentGuidance']


@admin.register(Guidances)
class GuidancesAdmin(admin.ModelAdmin):
    form = GuidancesAdminForm  # 改用使用了CKEditor的编辑器
    # list_display = ('GuidanceName', 'GuidanceContent',)
    list_display = ('GuidanceName', 'render_guidance_content')

    def render_guidance_content(self, obj):
        return mark_safe(obj.GuidanceContent)

@admin.register(ContainerManagement)
class ContainerManagementAdmin(admin.ModelAdmin):
    list_display = (
    'ContainerName', 'ContainerUser', 'ContainerImage', 'ContainerPorts', 'ContainerStartTime')
    search_fields = ['ContainerName', 'ContainerCourse']
    list_filter = ['ContainerUser', 'ContainerStartTime']
    fields = ['ContainerName', 'ContainerUser', 'ContainerImage', 'ContainerPorts',
              'ContainerStartTime']

    def has_add_permission(self, request):
        return False
