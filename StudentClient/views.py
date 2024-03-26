from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from GeneralInformation.models import ClassManagement, CourseManagement
from datetime import datetime

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
    CourseID = request.GET.get('id')
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


        # for Experiment in Course.Experiments:
        #     ExperimentName = Experiment.ExperimentName
        #     ExperimentInformation = Experiment.ExperimentInformation
