# Generated by Django 2.1.1 on 2018-12-06 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyblade_burst_web_app', '0014_auto_20181204_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energylayer',
            name='system',
            field=models.CharField(blank=True, choices=[('Burst', 'Burst'), ('Dual Layer', 'Dual Layer'), ('God', 'God Layer'), ('Chou-Z', 'Cho Z')], max_length=30),
        ),
    ]
