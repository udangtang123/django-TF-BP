# Generated by Django 3.2.11 on 2022-03-07 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0054_auto_20220308_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='costs',
            name='document',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='costs_doc', to='BP.doc'),
        ),
    ]