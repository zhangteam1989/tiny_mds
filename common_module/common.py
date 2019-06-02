#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ResultCode(object):
    def __init__(self, code, info):
        self._code = code
        self._info = info

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info

class Code(object):
    """
    10000-10999 定义user_center的错误
    """
    LOGIN_USERNAME_OR_PASSWORD_ERROR = ResultCode(10000, '用户名或密码错误')

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

    def __init__(self, status=0, data=None, msg=''):
        self._status = status
        self._data = data
        self._msg = msg

    @classmethod
    def fail_response(cls, code):
        """
        创建一个WebResult
        :type code: ResultCode
        """
        return cls(code.code, None, code.info)

    @classmethod
    def success_response(cls, data=None):
        """
        创建一个WebResult
        :type data: 响应数据
        """
        return cls(0, data, '')

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, msg):
        self._msg = msg
