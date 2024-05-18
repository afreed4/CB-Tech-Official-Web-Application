# Generated by Django 4.2.4 on 2023-08-05 05:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0003_alter_enquiry_next_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='course',
            field=models.OneToOneField(blank=True, choices=[(1, 'Python DJango '), (2, 'Python DJango '), (3, 'Python DJango ')], null=True, on_delete=django.db.models.deletion.CASCADE, to='cbtech_app.courses'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='declaration_type',
            field=models.CharField(choices=[('Digital', 'Digital'), ('Manual', 'Manual')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 4, 11, 2, 54, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status_of_enquiry',
            field=models.CharField(blank=True, choices=[('NotContacted', 'Not Contacted'), ('Contacted', 'Contacted'), ('Pending', 'Pending'), ('Interested', 'Interested'), ('NotInterested', 'Not Interested'), ('Registered', 'Registered')], default='Not Contacted', max_length=15, null=True),
        ),
    ]
