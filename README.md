# 计算资源利用率最大化资源共享平台
## 系统介绍
该系统通过Docker虚拟化技术将计算资源虚拟化、动态分配，系统用户可同时基于一台服务器快速开启多个Linux实验环境，快速搭建实验环境，且可进行实验指导内容编排，方便操作学习
![image](https://github.com/laishouchao/ResourceSharingExperimentPlatform/assets/55373024/4dbb0c9b-3805-4bea-90c2-85bfd2317e25)
![image](https://github.com/laishouchao/ResourceSharingExperimentPlatform/assets/55373024/577c21aa-2fdd-4794-83ff-e0ab50b8e902)
![image](https://github.com/laishouchao/ResourceSharingExperimentPlatform/assets/55373024/f72c0ff2-5bf3-4dba-a709-57af6d6a6488)

默认用户名密码
```
admin/admin
```

运行前安装Docker及Python

运行`pip install -r requirements.txt`安装所需的Python依赖文件

运行`python manage.py runserver`启动服务

也可通过Nginx部署至生产环境中
