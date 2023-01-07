# Generated by Django 3.2.11 on 2022-10-24 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0300_auto_20221025_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contact_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_contact1', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_contact2', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_contact3', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='emergency_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_emergency_contact', to='BP.emergencycontact'),
        ),
        migrations.AddField(
            model_name='client',
            name='mailing_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_mailing_contact', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='primary_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_primary_email', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='primary_phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_primary_phone', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]