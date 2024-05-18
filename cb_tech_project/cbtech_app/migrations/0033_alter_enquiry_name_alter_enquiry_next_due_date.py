# Generated by Django 5.0.4 on 2024-05-13 12:30

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtech_app', '0032_alter_enquiry_name_alter_enquiry_next_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='name',
            field=models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.DO_NOTHING, to='cbtech_app.attendence'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='next_due_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 22, 17, 1, 16, tzinfo=datetime.timezone.utc)),
        ),
    ]