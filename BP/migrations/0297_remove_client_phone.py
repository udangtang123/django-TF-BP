# Generated by Django 3.2.11 on 2022-10-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0296_auto_20221025_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='phone',
        ),
    ]