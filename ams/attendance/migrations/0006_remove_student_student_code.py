# Generated by Django 4.0.3 on 2022-03-11 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_remove_student_author_remove_student_banner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_code',
        ),
    ]
