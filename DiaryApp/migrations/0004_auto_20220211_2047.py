# Generated by Django 3.0.8 on 2022-02-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0003_auto_20220211_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarymodel',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]