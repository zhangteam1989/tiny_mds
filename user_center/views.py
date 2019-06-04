# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST, require_GET

from common_module.common import WebResult, Code
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_POST
def mds_login(request):
    username = request.POST.get('username', 'rooter')
    password = request.POST.get('password', 'root123456')
    # Django提供的authenticate函数，验证用户名和密码是否在数据库中匹配
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            # Django提供的login函数，将当前登录用户信息保存到会话key中
            login(request, user)
            return JsonResponse(WebResult.success_response(username=user.username))
        else:
            return JsonResponse(WebResult.fail_response(Code.LOGIN_USER_NOT_ACTIVE))
    else:
        # 返回用户名和密码错误信息
        return JsonResponse(WebResult.fail_response(Code.LOGIN_USERNAME_OR_PASSWORD_ERROR))


@require_GET
def mds_logout(request):
    # logout函数会清除当前用户保存在会话中的信息
    logout(request)