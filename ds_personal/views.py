#coding=utf-8

from PIL import Image
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ds_user import user_decorator
from .bitStatesUtils import *
from .models import *

#跳转到个人中心
@user_decorator.login
def personalHtml(request):
    username=request.session['user_name']
    context={'username':username,#用户名
             'currentMenu':'account'#左侧导航栏class　bootstrap样式
             }
    return render(request,'ds_personal/personal.html',context)

#跳转到实名认证
@user_decorator.login
def realAuthHtml(request):
    username = request.session['user_name']
    context = {'username':username,#用户名
             'currentMenu':'realAuth'#左侧导航栏class　bootstrap样式
             }
    return render(request,'ds_personal/realAuth.html',context)

#跳转到个人资料
@user_decorator.login
def userInfoHtml(request):
    user_id=request.session['user_id']
    username = request.session['user_name']
    #获取用户个人资料
    userInfo = UserInfo.objects.filter(pk=user_id)
    #用户是否实名认证
    if len(userInfo) :
        isRealAuth=hasState(userInfo.bitState,OP_REAL_AUTH)
    else:
        isRealAuth=False

    #获取学历数组
    educationBackgrounds=SystemDictionaryItem.objects.filter(parent_id=2)
    #获取月收入数组
    incomeGrades=SystemDictionaryItem.objects.filter(parent_id=1)
    #婚姻情况数组
    marrages = SystemDictionaryItem.objects.filter(parent_id=3)
    #子女情况数组
    kidCounts = SystemDictionaryItem.objects.filter(parent_id=4)
    #住房条件数组
    houseConditions = SystemDictionaryItem.objects.filter(parent_id=5)

    context = {'username': username,  # 用户名
               'currentMenu': 'userInfo' , # 左侧导航栏class　bootstrap样式
               'userInfo':userInfo,#用户信息
               'isRealAuth':isRealAuth,#是否已经实名认证
               'educationBackgrounds':educationBackgrounds,#学历选项
               "incomeGrades":incomeGrades,#月收入数组
               "marrages":marrages,#婚姻状况数组
               "kidCounts":kidCounts,#子女情况数组
               "houseConditions":houseConditions,#住房条件数组
               }
    return render(request, 'ds_personal/userInfo.html', context)

#上传图片

@csrf_exempt
@user_decorator.login
def realAuth_upload(request):
    imgFile=request.FILES['file']
    print imgFile