# Generated by Django 3.2.8 on 2021-11-20 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0007_auto_20211120_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availableleaves',
            old_name='teacher',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='leave',
            old_name='teacher',
            new_name='employee',
        ),
    ]
