# Generated by Django 2.1.1 on 2019-06-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyblade_burst_web_app', '0018_auto_20190605_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beybladepart',
            name='part_image',
            field=models.ImageField(blank=True, upload_to='parts/'),
        ),
    ]
