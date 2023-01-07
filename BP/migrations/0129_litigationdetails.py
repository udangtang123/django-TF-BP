# Generated by Django 3.2.11 on 2022-05-01 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0128_auto_20220501_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='LitigationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('time', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('department', models.CharField(default='', max_length=255, null=True)),
                ('litigation_type', models.CharField(default='', max_length=255, null=True)),
                ('zoom_link', models.TextField(blank=True, null=True)),
                ('for_case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_hearings', to='BP.case')),
                ('for_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BP.client')),
            ],
        ),
    ]