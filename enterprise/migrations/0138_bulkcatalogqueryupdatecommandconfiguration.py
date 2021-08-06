# Generated by Django 2.2.24 on 2021-08-02 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0137_enrollment_email_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkCatalogQueryUpdateCommandConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('arguments', models.TextField(blank=True, default='', help_text="Arguments for the 'bulk_update_catalog_query_id' management command. Specify like '<old ID> <new ID>'")),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
            ],
            options={
                'verbose_name': 'bulk_update_catalog_query_id argument',
            },
        ),
    ]