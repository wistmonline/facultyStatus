# Generated by Django 3.2.8 on 2021-10-24 06:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_attendance_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='location',
            field=models.CharField(choices=[('College Campus', 'College Campus'), ('AU', 'AU'), ('Counselling Duty', 'Counselling Duty'), ('Admission work', 'Admission work'), ('On Duty', 'On Duty'), ('Permission', 'Permission'), ('Leave', 'Leave'), ('other', 'other')], max_length=100),
        ),
    ]
