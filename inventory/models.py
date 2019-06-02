# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TInventory(models.Model):
    """
    库存数量表
    """
    id = models.CharField(primary_key=True, max_length=64)
    material_no = models.CharField(max_length=32)
    masc_code = models.CharField(max_length=4)
    location = models.IntegerField()
    qty = models.IntegerField()
    version = models.IntegerField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=64)
    update_time = models.DateTimeField()
    update_by = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_inventory'


class TInventoryChangeLog(models.Model):
    """
    库存变动日志
    """
    id = models.CharField(primary_key=True, max_length=32)
    inventory_id = models.CharField(max_length=64)
    qty = models.IntegerField()
    end_qty = models.IntegerField()
    location = models.IntegerField()
    action_type = models.IntegerField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_inventory_change_log'


class TInventoryImei(models.Model):
    """
    库存明细
    """
    id = models.CharField(primary_key=True, max_length=32)
    material_no = models.CharField(max_length=32)
    masc_code = models.CharField(max_length=4)
    imei = models.CharField(max_length=64)
    location = models.IntegerField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=64)
    update_time = models.DateTimeField()
    update_by = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_inventory_imei'
