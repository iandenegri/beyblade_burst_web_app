# Generated by Django 2.0.7 on 2018-12-04 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beyblade_burst_web_app', '0012_auto_20181204_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='combination',
            name='disk',
        ),
        migrations.RemoveField(
            model_name='combination',
            name='layer',
        ),
        migrations.RemoveField(
            model_name='combination',
            name='tip',
        ),
    ]
