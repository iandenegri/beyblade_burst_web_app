# Generated by Django 2.2.2 on 2019-09-23 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyblade_burst_web_app', '0020_auto_20190608_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beybladepart',
            name='product_code',
            field=models.IntegerField(blank=True, max_length=8),
        ),
    ]