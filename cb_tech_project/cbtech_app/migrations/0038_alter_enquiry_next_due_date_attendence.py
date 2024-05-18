# Generated by Django 5.0.4 on 2024-05-14 05:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0037_alter_enquiry_next_due_date_delete_attendence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 19, 52, 4, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendence_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField()),
                ('present', models.CharField(max_length=200, null=True)),
                ('absent', models.CharField(max_length=50, null=True)),
                ('connection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cbtech_app.enquiry')),
            ],
        ),
    ]