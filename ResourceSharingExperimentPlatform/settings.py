"""
Django settings for ResourceSharingExperimentPlatform project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os, time
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q_tor559dz!)$up_%4(-03#m!uq5=m8gr*%u8s0d*k%vt5u#&+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',  # admindoc模块
    'GeneralInformation.apps.GeneralinformationConfig',
    'EnvironmentalInformation.apps.EnvironmentalinformationConfig',
    'SystemSettings.apps.SystemsettingsConfig',
    'StudentClient.apps.StudentclientConfig',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ResourceSharingExperimentPlatform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ResourceSharingExperimentPlatform.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/SimpleUI")
STATICFILES_DIRS = [BASE_DIR / "static"]

# CKeditor 编辑器设置
CKEDITOR_UPLOAD_PATH = "ckeditor/"  # 文件上传路径

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['RemoveFormat', 'Source']
        ],
    },
}

CKEDITOR_FILE_UPLOADER = "ckeditor_uploader.uploader.CKEditorFileUploader"
CKEDITOR_JQUERY_URL = 'https://cdn.bootcss.com/jquery/2.2.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SIMPLEUI关闭服务器信息
SIMPLEUI_HOME_INFO = False
# SIMPLEUI关闭快捷菜单
# SIMPLEUI_HOME_QUICK = False
# SIMPLEUI关闭历史操作记录
# SIMPLEUI_HOME_ACTION = False
# SIMPLEUI关闭使用分析
SIMPLEUI_ANALYSIS = False
# SIMPLEUI设置默认主题
SIMPLEUI_DEFAULT_THEME = 'generic.css'
# SIMPLEUI启用离线资源
SIMPLEUI_STATIC_OFFLINE = True
# SIMPLEUI LOGO
SIMPLEUI_LOGO = '/static/logo.jpg'

SIMPLEUI_CONFIG = {
    'system_keep': True,
    'menu_display': ['课程管理', '基础 环境', '认证和授权', '系统配置'],  # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,  # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [{'app': 'GeneralInformation',
               'name': '课程管理',
               'icon': 'fas fa-book-reader',
               'models': [{
                   'name': '专业班级',
                   'icon': 'fas fa-user-graduate',
                   'url': 'GeneralInformation/classmanagement/',
               }, {
                   'name': '课时管理',
                   'icon': 'fas fa-vials',
                   'url': 'GeneralInformation/coursemanagement/',
               }, {
                   'name': '实验容器',
                   'icon': 'fas fa-box',
                   'url': 'GeneralInformation/containermanagement/',
               }, {
                   'name': '实验报告',
                   'icon': 'fas fa-file-word',
                   'url': 'GeneralInformation/experimentalreport/',
               },
               ]},

              {'app': 'EnvironmentalInformation',
               'name': '基础 环境',
               'icon': 'fas fa-flask',
               'models': [{
                   'name': '实验指导书',
                   'icon': 'fas fa-book-open',
                   'url': 'EnvironmentalInformation/guidances/',
               }, {
                   'name': '实验基础环境',
                   'icon': 'fas fa-vials',
                   'url': 'EnvironmentalInformation/experiments/',
               }]
               },
              {
                  'name': '系统配置',
                  'icon': 'fas fa-cogs',
                  'url': '/admin/SystemSettings/systemsetting/1/change/',
                  # 浏览器新标签中打开
                  'newTab': False,
              }]
}

DJANGO_SETTINGS_MODULE = ''

# 登录成功后跳转回主页
LOGIN_URL = '/Login/'
LOGIN_REDIRECT_URL = '/'
