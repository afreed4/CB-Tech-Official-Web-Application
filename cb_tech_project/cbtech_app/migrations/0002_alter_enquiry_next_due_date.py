# Generated by Django 4.2.3 on 2023-07-31 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 3, 6, 0, 37, tzinfo=datetime.timezone.utc)),
        ),
    ]