# Generated by Django 5.0.4 on 2024-05-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_enquery'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquery',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
