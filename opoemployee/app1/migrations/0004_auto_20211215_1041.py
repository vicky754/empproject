# Generated by Django 3.2.9 on 2021-12-15 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20211215_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_of_joining',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='emp_image',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='reporting_manager',
        ),
    ]
