# Generated by Django 3.2.8 on 2022-06-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0009_rename_leave_category_leave_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='emergency',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
