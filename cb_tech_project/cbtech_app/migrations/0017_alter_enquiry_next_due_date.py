# Generated by Django 4.2.4 on 2023-08-21 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0016_enquiry_payment_date_enquiry_payment_receipt_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 3, 11, 1, 25, tzinfo=datetime.timezone.utc)),
        ),
    ]
