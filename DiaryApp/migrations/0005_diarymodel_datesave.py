# Generated by Django 3.0.8 on 2022-02-11 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0004_auto_20220211_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarymodel',
            name='datesave',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
