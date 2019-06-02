# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from common_module.common import WebResult, Code
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    # Django提供的authenticate函数，验证用户名和密码是否在数据库中匹配
    user = authenticate(username=username, password=password)
    if user is not None:
        # Django提供的login函数，将当前登录用户信息保存到会话key中
        login(request, user)
        return JsonResponse(WebResult.success_response(user))
    else:
        # 返回用户名和密码错误信息
        return JsonResponse(WebResult.fail_response(Code.LOGIN_USERNAME_OR_PASSWORD_ERROR))


def logout(request):
    # logout函数会清除当前用户保存在会话中的信息
    logout(request)
