# Generated by Django 5.0.4 on 2024-05-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_sportsandarts_end_date_alter_venue_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsandarts',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='venue',
            name='start_date',
            field=models.DateField(),
        ),
    ]