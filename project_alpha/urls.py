"""project_alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from project_alpha.page2 import page2
from project_alpha.page1 import page1
from project_alpha.app2 import app2
from project_alpha.app3 import app3
from project_alpha.app1 import app1
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', app3),
    path('admin/app1', app1),
    path('admin/app2/hello', app2),
    path('admin/app1/page1', page1),
    path('admin/app1/page2', page2),
]
