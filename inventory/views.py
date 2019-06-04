# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
from common_module.common import WebResult
from inventory.api import InventoryImeiApi


@require_GET
def query_inventory_page(request):
    """
    分页查询库存记录
    :param request:
    :return:
    """
    print('sadfasfas')


@require_GET
def query_one_inventory_imei(request):
    """
    根据material_no和masc_code加载库存明细
    :param request:
    :return:
    """
    imei = request.GET.get('imei','')
    data = {}
    if imei:
        data = InventoryImeiApi.find_one_by_imei(imei)
        data = model_to_dict(data)
        if data is None:
            data = {}
    return JsonResponse(WebResult.success_response(**data))


@require_POST
def change_inventory(request):
    """
    库存变动信号,通过接口触发库存变动
    :param request:
    :return:
    """
    pass
