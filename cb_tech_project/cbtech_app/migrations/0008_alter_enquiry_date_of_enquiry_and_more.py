# Generated by Django 4.2.4 on 2023-08-13 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0007_rename_alternative_phone_number_enquiry_alternate_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='date_of_enquiry',
            field=models.DateField(default=datetime.datetime(2023, 8, 13, 16, 17, 57, 635072, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 5, 12, 16, tzinfo=datetime.timezone.utc)),
        ),
    ]
