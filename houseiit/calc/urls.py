# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:47:13 2020

@author: Hitesh
"""


from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path("add",views.add,name="add"),
    path("sub",views.sub,name="sub"),
    path("mul",views.mul,name="mul"),
    ]