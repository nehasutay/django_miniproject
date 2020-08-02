"""project URL Configuration

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
from app import views

urlpatterns = [
    path('',views.member,name='member'),
    path('home/',views.home,name='home'),
    path('loan/',views.loan,name='loan'),
    # path('emi/',views.emi,name='emi'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('profile/',views.profile,name='profile'),
    path('transactionmain/',views.transactionmain,name='transactionmain'),
    path('admin1/',views.admin1,name='admin1'),
    # path('member/',views.member,name='member'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    # path('loginpage/',views.loginpage,name='loginpage'),
    #path('register/',views.register,name='register'),
    path('formupload/',views.formupload,name='formupload'),
    path('seeprofile/',views.seeprofile,name='seeprofile'),
    path('seedetails/',views.seedetails,name='seedetails'),
    path('trans/',views.trans,name='trans'),
    path('transdis/',views.transdis,name='transdis'),
    path('status/',views.status,name='status'),
    path('apply/',views.apply,name='apply'),
    

]
