import random
from datetime import datetime

import docker
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

import GeneralInformation.models
from EnvironmentalInformation.models import Experiments
from GeneralInformation.models import CourseManagement, ContainerManagement
from SystemSettings.models import SystemSetting


# Create your views here.
# @login_required
def GetIndexPage(request):
    user = request.user
    SelectCourseInfos = CourseManagement.objects.all().order_by('CourseStartTime')
    paginator = Paginator(SelectCourseInfos, 5)
    page = request.GET.get('page')
    try:
        CourseInfos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        CourseInfos = paginator.page(1)
    except EmptyPage:
        CourseInfos = paginator.page(paginator.num_pages)
    return render(request, "StudentClient/index.html", {'CourseInfos': CourseInfos, 'user': user})


@login_required
def GetCoursePage(request):
    CourseID = request.GET.get('CourseID')
    Course = CourseManagement.objects.filter(id__exact=CourseID)[0]
    # 判断权限
    CurrentTime = datetime.now()
    if CurrentTime > Course.CourseStopTime.replace(tzinfo=None):
        print("课程已经过期关闭")
        return HttpResponse("<script>alert`课程已经过期关闭`;history.go(-1);location.reload();</script>", status=403)
    elif CurrentTime < Course.CourseStartTime.replace(tzinfo=None):
        print("课程尚未到达开放时间")
        return HttpResponse("<script>alert`课程尚未到达开放时间`;history.go(-1);location.reload();</script>", status=403)
    elif request.user in Course.JoinUsers.all():
        # 鉴权通过，返回课程内容
        print("当前用户有权限参与课程")
        return render(request, "StudentClient/course.html", {'Course': Course, 'user': request.user})
    else:
        print("当前用户没有课程权限")
        return HttpResponse("<script>alert`当前用户没有课程权限`;history.go(-1);location.reload();</script>", status=403)


class CreateDocker:
    def __init__(self):
        while True:
            # 查询数据库中定义的生成端口范围
            self.RandomPort = random.randint(SystemSetting.objects.all()[0].PortRangeStart,
                                             SystemSetting.objects.all()[0].PortRangeStop)
            if ContainerManagement.objects.filter(ContainerPorts__exact=self.RandomPort):
                continue
            else:
                print("本次将创建容器实例，映射到端口 ", self.RandomPort)
                break

    def creat_docker_by_dockerhub(self, dockerHub, Port):
        client = docker.from_env()
        client.images.pull(dockerHub)
        Container = client.containers.run(image=dockerHub,
                                          # command='/bin/sh -c "while true; do echo hello world; sleep 1; done"',
                                          ports={Port: self.RandomPort}, detach=True)
        return Container, self.RandomPort


@login_required
def ExperimentPage(request):
    CourseID = request.GET.get('CourseID')
    ExperimentID = request.GET.get('ExperimentID')
    User = request.user
    # 查询是否已经有ContainerManagement对象存在
    if not ContainerManagement.objects.filter(ContainerUser_id__exact=request.user.id).filter(
            ContainerCourse_id__exact=CourseID).filter(ContainerImage_id__exact=ExperimentID):
        # 不存在容器
        # 查询实验环境对应的镜像信息，端口等
        Experiment = Experiments.objects.filter(id__exact=ExperimentID)[0]
        Image = Experiment.ExperimentImage
        Ports = Experiment.ExperimentPorts
        # 创建容器
        Container, Port = CreateDocker().creat_docker_by_dockerhub(dockerHub=Image, Port=Ports)
        # 创建ContainerManagement对象，将容器信息、课程信息、映射端口等信息进行保存
        Container_temp = GeneralInformation.models.ContainerManagement()
        Container_temp.ContainerName = Container.name
        Container_temp.ContainerCode = Container.id
        Container_temp.ContainerCourse = CourseManagement.objects.filter(id__exact=CourseID)[0]
        Container_temp.ContainerUser = User
        Container_temp.ContainerImage = Experiment
        Container_temp.ContainerPorts = Port
        Container_temp.ContainerStartTime = datetime.now()
        Container_temp.save()
    # 存在容器，返回实验界面信息,直接返回容器界面等信息
    Container = ContainerManagement.objects.filter(ContainerUser_id__exact=request.user.id).filter(
        ContainerCourse_id__exact=CourseID).filter(ContainerImage_id__exact=ExperimentID)[0]
    IPsetting = SystemSetting.objects.all()[0].IPSetting
    return render(request, "StudentClient/Experiment.html",
                  {'Container': Container, 'IPsetting': IPsetting, 'user': request.user})


# 注册功能
def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = UserCreationForm()
    return render(request, 'StudentClient/register.html', {'form': form})


def UploadExperimentalReport(request):
    CourseID = request.POST.get('CourseID')
    User = request.user
    ReportFile = request.POST.get('file')
    UploadTime = datetime.now().replace(tzinfo=None)
    print(CourseID, ReportFile)
    Report = GeneralInformation.models.ExperimentalReport()
    Report.Course = CourseManagement.objects.filter(id__exact=CourseID)[0]
    Report.User = User
    Report.ReportFile = ReportFile
    Report.UploadTime = UploadTime
    Report.save()
    return HttpResponse("<script>alert`上传成功。`;history.go(-1);location.reload();</script>", status=200)
