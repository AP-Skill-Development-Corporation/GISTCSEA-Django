"""GISTProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from GISTApp import views
from Bootapp import views as bt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rs/',views.dsmsg),
    path('av/',views.eve),
    path('sdt/<str:n>/',views.stdtls),
    path('emp/<str:na>/<int:eid>/',views.empd),
    path('dc/<str:name>/',views.gh),
    path('fg/<str:en>/<str:eid>/<int:age>/',views.ed),
    path('jk/',views.hk),
    path('jkc/',views.hkm),
    path('jm/<str:na>/',views.gm),
    path('h/',views.k),
    path('r/<str:er>/',views.stf),
    path('v/<str:n>/<int:ag>/',views.dt),
    path('rg/',views.reg,name="bk"),
    path('',bt.home,name="hm"),
    path('aby/',bt.abt,name="ab"),
    path('g/',bt.grid,name="gd"),
    path('rd/',bt.stdr,name="rg"),
]


