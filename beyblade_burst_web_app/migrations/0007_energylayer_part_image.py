# Generated by Django 2.0.7 on 2018-11-28 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyblade_burst_web_app', '0006_auto_20181128_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='energylayer',
            name='part_image',
            field=models.ImageField(blank=True, upload_to='parts/layers/'),
        ),
    ]