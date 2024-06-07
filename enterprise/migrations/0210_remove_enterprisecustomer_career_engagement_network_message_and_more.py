# Generated by Django 4.2.10 on 2024-06-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0209_alter_enterprisecustomer_disable_expiry_messaging_for_learner_credit_and_more'),
    ]

    # operations = [
    #     migrations.RemoveField(
    #         model_name='enterprisecustomer',
    #         name='career_engagement_network_message',
    #     ),
    #     migrations.RemoveField(
    #         model_name='enterprisecustomer',
    #         name='enable_career_engagement_network_on_learner_portal',
    #     ),
    #     migrations.RemoveField(
    #         model_name='historicalenterprisecustomer',
    #         name='career_engagement_network_message',
    #     ),
    #     migrations.RemoveField(
    #         model_name='historicalenterprisecustomer',
    #         name='enable_career_engagement_network_on_learner_portal',
    #     ),
    #     migrations.AddField(
    #         model_name='enterprisecustomer',
    #         name='enable_learner_portal_sidebar_message',
    #         field=models.BooleanField(default=False, help_text='If checked, learners will be able to see content in the Learner Portal Sidebar found in the HTML box.', verbose_name='Enable learner portal sidebar message'),
    #     ),
    #     migrations.AddField(
    #         model_name='enterprisecustomer',
    #         name='learner_portal_sidebar_content',
    #         field=models.TextField(blank=True, help_text='Text shown on the learner portal dashboard for customer specific purposes. Open HTML field.'),
    #     ),
    #     migrations.AddField(
    #         model_name='historicalenterprisecustomer',
    #         name='enable_learner_portal_sidebar_message',
    #         field=models.BooleanField(default=False, help_text='If checked, learners will be able to see content in the Learner Portal Sidebar found in the HTML box.', verbose_name='Enable learner portal sidebar message'),
    #     ),
    #     migrations.AddField(
    #         model_name='historicalenterprisecustomer',
    #         name='learner_portal_sidebar_content',
    #         field=models.TextField(blank=True, help_text='Text shown on the learner portal dashboard for customer specific purposes. Open HTML field.'),
    #     ),
    # ]

    # We gonna write our own migration to rename the fields instead of removing them
    operations = [
        migrations.RenameField(
            model_name='enterprisecustomer',
            old_name='career_engagement_network_message',
            new_name='learner_portal_sidebar_content',
        ),
        migrations.RenameField(
            model_name='enterprisecustomer',
            old_name='enable_career_engagement_network_on_learner_portal',
            new_name='enable_learner_portal_sidebar_message',
        ),
        migrations.RenameField(
            model_name='historicalenterprisecustomer',
            old_name='career_engagement_network_message',
            new_name='learner_portal_sidebar_content',
        ),
        migrations.RenameField(
            model_name='historicalenterprisecustomer',
            old_name='enable_career_engagement_network_on_learner_portal',
            new_name='enable_learner_portal_sidebar_message',
        ),
    ]
