# Generated by Django 3.0.8 on 2022-02-11 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0006_auto_20220211_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diarymodel',
            name='imageupload',
        ),
    ]