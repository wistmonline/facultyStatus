# Generated by Django 3.2.8 on 2021-11-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0006_auto_20211120_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='hod_approved',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='principal_approved',
            field=models.BooleanField(null=True),
        ),
    ]
