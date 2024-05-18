# Generated by Django 4.2.4 on 2023-08-10 07:31

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0004_alter_enquiry_course_alter_enquiry_declaration_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='repeated_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date_repeated', models.DateField(auto_now=True)),
                ('last_enquiry_date', models.DateField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='date_of_registeration',
            new_name='date_of_registration',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='phone_no',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='enquiry',
            old_name='student_registeration_id',
            new_name='student_registration_id',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 24, 23, 52, 33, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Paid', 'Paid'), ('NotPaid', 'Not Paid'), ('PartiallyPaid', 'Partially Paid'), ('EMI', 'EMI')], default='Not Paid', max_length=15, null=True),
        ),
    ]
