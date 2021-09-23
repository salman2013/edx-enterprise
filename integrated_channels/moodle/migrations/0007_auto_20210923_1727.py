# Generated by Django 2.2.24 on 2021-09-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0006_auto_20210909_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmoodleenterprisecustomerconfiguration',
            name='disable_learner_data_transmissions',
            field=models.BooleanField(default=False, help_text='When set to True, the configured customer will no longer receive learner data transmissions, both scheduled and signal based', verbose_name='Disable Learner Data Transmission'),
        ),
        migrations.AddField(
            model_name='moodleenterprisecustomerconfiguration',
            name='disable_learner_data_transmissions',
            field=models.BooleanField(default=False, help_text='When set to True, the configured customer will no longer receive learner data transmissions, both scheduled and signal based', verbose_name='Disable Learner Data Transmission'),
        ),
    ]
