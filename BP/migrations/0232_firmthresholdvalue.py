# Generated by Django 3.2.11 on 2022-09-14 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0231_alter_caseproviders_for_case'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirmThresholdValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_damage_value', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('for_firm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firm_threshold_values', to='BP.attorney')),
            ],
        ),
    ]