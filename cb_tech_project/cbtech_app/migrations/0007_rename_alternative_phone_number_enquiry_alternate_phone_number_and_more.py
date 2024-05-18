# Generated by Django 4.2.4 on 2023-08-13 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0006_remove_enquiry_alternative_phone_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='alternative_phone_number',
            new_name='alternate_phone_number',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='staff_type',
            field=models.CharField(choices=[('Admin', 'Administrator'), ('Faculty', 'Faculty'), ('Counsellor', 'Counsellor'), ('Accountant', 'Accountant'), ('Manager', 'Marketing Manager')], max_length=12),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 15, 2, 38, 53, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='office',
            field=models.CharField(blank=True, default='Kadavanthra', max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='reference_contact_number',
            field=models.CharField(blank=True, default='', max_length=15, null=True),
        ),
    ]