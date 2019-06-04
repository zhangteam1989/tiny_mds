# -*- coding: utf-8 -*-
from models import TInventory, TInventoryImei, TInventoryChangeLog


class InventoryApi(object):

    @staticmethod
    def add_inventory():
        """
        增加库存
        :return:
        """
        pass

    @staticmethod
    def move_inventory():
        """
        移动库存
        :return:
        """
        pass

    @staticmethod
    def remove_inventory():
        """
        扣减库存
        :return:
        """
        pass


class InventoryImeiApi(object):

    @staticmethod
    def find_one_by_imei(imei=''):
        imei_list = TInventoryImei.objects.filter(imei=imei)
        return imei_list.first()
