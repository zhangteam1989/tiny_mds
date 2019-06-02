# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def query_inventory_page(request):
    """
    分页查询库存记录
    :param request:
    :return:
    """
    pass


def query_inventory_imei(request):
    """
    根据material_no和masc_code加载库存明细
    :param request:
    :return:
    """
    pass


def change_inventory(request):
    """
    库存变动信号,通过接口触发库存变动
    :param request:
    :return:
    """
    pass
