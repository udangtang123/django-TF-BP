# Generated by Django 3.2.11 on 2022-10-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0276_auto_20221016_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]