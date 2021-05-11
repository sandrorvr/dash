# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dados(models.Model):
    partition_country = models.TextField(blank=True, null=True)
    kpi1 = models.TextField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    vin_hash = models.IntegerField(blank=True, null=True)
    production_date = models.TextField(blank=True, null=True)
    countnull_n_expected = models.IntegerField(db_column='countNull_N_expected', blank=True, null=True)  # Field name made lowercase.
    vin = models.IntegerField(blank=True, null=True)
    vin_vl = models.IntegerField(blank=True, null=True)
    response_ecu_id = models.TextField(blank=True, null=True)
    did_id = models.TextField(blank=True, null=True)
    partition_region = models.TextField(blank=True, null=True)
    kpi9 = models.TextField(blank=True, null=True)
    derived_event = models.TextField(blank=True, null=True)
    kpi2 = models.TextField(blank=True, null=True)
    vehicle_line = models.TextField(blank=True, null=True)
    sell_country = models.TextField(blank=True, null=True)
    kpi5 = models.TextField(blank=True, null=True)
    kpi6 = models.TextField(blank=True, null=True)
    kpi7 = models.TextField(blank=True, null=True)
    kpi4 = models.TextField(blank=True, null=True)
    countnull_expected = models.IntegerField(db_column='countNull_expected', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'DADOS'
