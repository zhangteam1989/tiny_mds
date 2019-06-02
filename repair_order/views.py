# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def create_order(request):
    """
    创建订单
    1.订单号自动生成,订单号=RO+yyyyMMddHHmmss+5位数序列号
    2.库存已经存在的imei不允许建单
    3.同一个imei不允许存在非完结订单
    :param request:
    :return:
    """
    pass


def submit_order(request):
    """
    提交订单
    只有待提交状态的订单才能submit
    :param request:
    :return:
    """
    pass


def receipt(request):
    """
    收货
    1.只有submit状态的订单才能收货
    2.校验imei是否已经在库存中存在,存在则不允许收货
    3.收货,坏件库位数量+1
    4.修改收货状态为已收货
    :param request:
    :return:
    """
    pass


def repair(request):
    """
    维修
    1.只有已收货订单才能进行维修
    :param request:
    :return:
    """
    pass


def ship(request):
    """
    发货
    :param request:
    :return:
    """
    pass


def update_customer_info(request):
    """
    更新客户信息
    :param request:
    :return:
    """
    pass


def cancel_order(request):
    """
    取消订单
    :param request:
    :return:
    """
    pass


def query_order_page(request):
    """
    分页查询订单
    :param request:
    :return:
    """
    pass


def load_order(request):
    """
    根据订单编号加载订单数据
    :param request:
    :return:
    """
    pass


