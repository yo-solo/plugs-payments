# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-09 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plugs_payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MBPayment',
            new_name='IfThenPayment',
        ),
        migrations.AlterModelOptions(
            name='ifthenpayment',
            options={'verbose_name': 'payment', 'verbose_name_plural': 'payments'},
        ),
    ]
