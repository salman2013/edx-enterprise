# Generated by Django 3.2.19 on 2023-07-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0175_auto_20230629_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisecustomer',
            name='auth_org_id',
            field=models.CharField(blank=True, help_text="Enterprise customer's authentication ID ", max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='historicalenterprisecustomer',
            name='auth_org_id',
            field=models.CharField(blank=True, help_text="Enterprise customer's authentication ID ", max_length=80, null=True),
        ),
    ]