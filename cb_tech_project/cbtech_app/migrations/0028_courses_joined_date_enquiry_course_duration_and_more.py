# Generated by Django 5.0.4 on 2024-05-06 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0027_enquiry_certificate_enquiry_exam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='joined_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='course_duration',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Crash', 'Crash'), ('Project', 'Project')], default='4 Months', max_length=25),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='course_type',
            field=models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Crash', 'Crash'), ('Project', 'Project')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='joined_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 7, 22, 18, 23, tzinfo=datetime.timezone.utc)),
        ),
    ]