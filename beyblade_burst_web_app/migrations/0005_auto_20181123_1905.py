# Generated by Django 2.0.7 on 2018-11-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyblade_burst_web_app', '0004_auto_20181123_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='energylayer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='forgedisk',
            name='id',
        ),
        migrations.RemoveField(
            model_name='performancetip',
            name='id',
        ),
        migrations.AlterField(
            model_name='energylayer',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='forgedisk',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='performancetip',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=8, primary_key=True, serialize=False),
        ),
    ]
