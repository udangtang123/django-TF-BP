# Generated by Django 3.2.11 on 2022-10-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0260_company_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defendant',
            name='liability_insurance_id',
        ),
        migrations.AddField(
            model_name='defendant',
            name='liability_insurance_id',
            field=models.ManyToManyField(blank=True, related_name='defendant_liability_insurance_id', to='BP.Insurance'),
        ),
    ]