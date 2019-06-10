# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST, require_GET

from common_module.common import WebResult, Code
from django.views.decorators.csrf import csrf_exempt


def mds_index(request):
    name = request.user.username  # 通过user拿到相关信息
    return render(request, 'index.html', {'user': name})


@csrf_exempt
def mds_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'rooter')
        password = request.POST.get('password', 'root123456')
        # Django提供的authenticate函数，验证用户名和密码是否在数据库中匹配
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # Django提供的login函数，将当前登录用户信息保存到会话key中
                login(request, user)
                return redirect('/user/index/')
            else:
                # return JsonResponse(WebResult.fail_response(Code.LOGIN_USER_NOT_ACTIVE))
                return render(request, 'login.html', {'error': '用户未激活', 'username': username, 'password': password})
        else:
            # 返回用户名和密码错误信息
            # return JsonResponse(WebResult.fail_response(Code.LOGIN_USERNAME_OR_PASSWORD_ERROR))
            return render(request, 'login.html', {'error': '用户名或密码错误', 'username': username, 'password': password})
    return render(request, 'login.html')


@require_GET
def mds_logout(request):
    # logout函数会清除当前用户保存在会话中的信息
    logout(request)
