#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from models import *
from hashlib import sha1


#注册界面
def register(request):
    return render(request,'ds_user/register.html')
#验证用户名是否存在
def registerNameCheck(request):
    username=request.GET['username']
    print request.GET
    print "====================="
    print username
    count=usernameCount(username)
    context={'count' : count}
    return JsonResponse(context)

#检查用户名个数
def usernameCount(username):
    count = LoginInfo.objects.filter(username=username).count()
    return count

#加密
def setPasswordSha(password):
    s1 = sha1()
    s1.update(password)
    pwd = s1.hexdigest()
    return pwd

#执行注册
def registerSubmit(request):
    username = request.POST['username']
    count = usernameCount(username)
    if (count > 0):
        return JsonResponse({'count': count})
    else:
        try:
            #密码加密
            password=request.POST['password']
            pwd=setPasswordSha(password)
            info=LoginInfo()
            info.username=username
            info.password=pwd
            info.save()
            context={'success':True}
            return JsonResponse(context)
        except:
            context = {'success': False}
            return JsonResponse(context)

#登录页面
def login(request):
    return render(request,'ds_user/login.html')

#登录submit
def loginSubmit(request):
    post=request.POST
    username=post.get('username')
    password=post.get('password')

    info=LoginInfo.objects.filter(username=username)
    #判断用户是否存在
    if len(info)==0 :
        context = jsonSet(False,'登录失败!')
        return JsonResponse(context)
    user=info[0]
    if(setPasswordSha(password)!=user.password):
        return JsonResponse(jsonSet(False,'登录失败！'))

    request.session['user_id']=user.id
    request.session['user_name']=user.username

    return JsonResponse(jsonSet(True,'登录成功!'))

#json封装
def jsonSet(isSuccess, msg):
    context = {'success': isSuccess, 'msg': msg}
    return context