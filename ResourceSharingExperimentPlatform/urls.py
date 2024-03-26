"""ResourceSharingExperimentPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView
import StudentClient.views

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    path('Login/', LoginView.as_view(template_name='StudentClient/login.html', success_url='/'), name='Login'),
    path('Logout/', LogoutView.as_view(next_page='/'), name="Logout"),
    path('PasswordChange/', PasswordChangeView.as_view(), name='PasswordChange'),
    path('PasswordReset/', PasswordResetView.as_view(), name='PasswordReset'),

    path('', StudentClient.views.GetIndexPage),  # 系统主页，显示所有的课程信息
    path('Course/', StudentClient.views.GetCoursePage),  # 课程页面，显示所有的实验


    # path('hello', pingtai.views.HelloWorld),  # 环境测试函数
    # path('match/', pingtai.views.getMatchPage),  # 比赛详情
    # path('push/', pingtai.views.pushFlag),  # 提交flag
    # path('notice/', pingtai.views.getNotic),  # 公告模块
    # path('creatDocker/', pingtai.views.CreateDocker),  # 创建Docker环境 未完成
    # path('getuploadWriteUpFilePage/', pingtai.views.getuploadWriteUpFilePage),  # 提交WriteUp页面
    # path('uploadwp/', pingtai.views.uploadWritefile),  # 接受上传的WP
    # path('anticheating/', pingtai.views.getAntiCheatingPage),  # 烽火台
    # path('createDockerContainer/', pingtai.views.createDockerContainer),  # 创建Docker容器实例
    # path('rank/', pingtai.views.Rank),  # 排名
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
