#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ResultCode(object):
    def __init__(self, code, info):
        self.code = code
        self.info = info


class Code(object):
    """
    10000-10999 定义user_center的错误
    """
    LOGIN_USERNAME_OR_PASSWORD_ERROR = ResultCode(10000, '用户名或密码错误')
    LOGIN_USER_NOT_ACTIVE = ResultCode(10001, '用户未激活')

    """
    20000-20999 定义basis data相关错误编码
    """

    """
    21000-21999 定义repair order相关错误编码
    """

    """
    22000-21999 定义inventory相关错误编码
    """


class WebResult(object):

    def __init__(self, status=0, msg=None, **data):
        self.status = status
        self.data = data
        self.msg = msg

    @classmethod
    def fail_response(cls, result_code, **data):
        """
        创建一个WebResult
        :type result_code: ResultCode
        """
        return cls(result_code.code, result_code.info, **data).__dict__

    @classmethod
    def success_response(cls, **data):
        """
        创建一个WebResult
        :type data: 响应数据
        """
        return cls(0, None, **data).__dict__

