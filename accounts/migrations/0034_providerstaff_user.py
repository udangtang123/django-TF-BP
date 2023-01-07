# Generated by Django 3.2.11 on 2022-02-02 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0033_providerstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='providerstaff',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='providerstaff_userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]