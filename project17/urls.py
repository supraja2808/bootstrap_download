"""
URL configuration for project17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bootstrap_download/',bootstrap_download,name='bootstrap_download'),
    path('modal/',modal,name='modal'),
     path('navs/',navs,name='navs'),
     path('navbar/',navbar,name='navbar'),
     path('pagination/',pagination,name='pagination'),
       path('popovers/',popovers,name='popovers'),
       path('progress/',progress,name='progress'),
       path('scrollspy/',scrollspy,name='scrollspy'),
       path('spinners/',spinners,name='spinners'),
       path('toasts/',toasts,name='toasts'),
       path('tooltips/',tooltips,name='tooltips'),
]

