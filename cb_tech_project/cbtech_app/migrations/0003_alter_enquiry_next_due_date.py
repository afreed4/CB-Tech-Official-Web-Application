# Generated by Django 4.2.3 on 2023-08-01 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0002_alter_enquiry_next_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 2, 43, 19, tzinfo=datetime.timezone.utc)),
        ),
    ]