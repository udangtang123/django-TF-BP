# Generated by Django 3.2.11 on 2022-02-20 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0016_witness'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=255)),
                ('policy_no', models.CharField(default='', max_length=255)),
                ('claim_no', models.CharField(default='', max_length=255)),
                ('adjuster_name', models.CharField(default='', max_length=255)),
                ('adjuster_address', models.CharField(default='', max_length=255)),
                ('adjuster_phone', models.CharField(default='', max_length=255)),
                ('adjuster_fax', models.CharField(default='', max_length=255)),
                ('adjuster_email', models.CharField(default='', max_length=255)),
                ('for_defendant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='defendant_insurances', to='BP.defendant')),
            ],
        ),
    ]