# Generated by Django 3.2.20 on 2023-09-14 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0183_auto_20230906_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomerssoconfiguration',
            name='first_name_attribute',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomerssoconfiguration',
            name='first_name_attribute',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]