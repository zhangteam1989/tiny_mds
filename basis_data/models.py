# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TBasisCost(models.Model):
    """
    费用类型
    """
    id = models.IntegerField(primary_key=True)
    cost_name = models.CharField(max_length=64)
    cost_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_basis_cost'


class TBasisLocation(models.Model):
    """
    库位类型,0-坏件,1-翻新,2-未开封整机,3-废件,4在途
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_basis_location'


class TBasisSbom(models.Model):
    """
    物料配置
    material_no: 物料编号
    """
    id = models.CharField(primary_key=True, max_length=32)
    material_no = models.CharField(unique=True, max_length=32)
    description = models.CharField(max_length=512)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=64)
    update_time = models.DateTimeField()
    update_by = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_basis_sbom'
