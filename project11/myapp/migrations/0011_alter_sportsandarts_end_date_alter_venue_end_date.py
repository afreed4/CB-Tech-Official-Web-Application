# Generated by Django 5.0.4 on 2024-05-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_sportsandarts_landmark_alter_venue_landmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsandarts',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]
