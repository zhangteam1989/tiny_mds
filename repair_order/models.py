# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TRepairOrder(models.Model):
    order_no = models.CharField(primary_key=True, max_length=32)
    receipt_status = models.IntegerField()
    ship_status = models.IntegerField()
    status = models.IntegerField()
    imei = models.CharField(max_length=64)
    customer = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    contact_phone = models.CharField(max_length=16)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=64)
    update_time = models.DateTimeField()
    update_by = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_repair_order'


class TRepairOrderCost(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    order_no = models.CharField(max_length=32)
    cost_type = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 't_repair_order_cost'


class TRepairOrderLogistics(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    type = models.CharField(max_length=16)
    tracking_no = models.CharField(max_length=32)
    order_no = models.ForeignKey(TRepairOrder, models.DO_NOTHING, db_column='order_no')
    picking_time = models.DateTimeField(blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_repair_order_logistics'


class TRepairOrderStatusLog(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    order_no = models.ForeignKey(TRepairOrder, models.DO_NOTHING, db_column='order_no')

    class Meta:
        managed = False
        db_table = 't_repair_order_status_log'


class TRepairOrderSequence(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)

    class Meta:
        managed = False
        db_table = 't_repair_order_sequence'

    @classmethod
    def acquire_sequence(cls):
        ros = TRepairOrderSequence.objects.create()
        id_str = str(ros.id)[:5]
        return '00000'[:5-len(id_str)] + id_str

