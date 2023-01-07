# Generated by Django 3.2.11 on 2022-01-30 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_review_post_as'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketer_code', models.CharField(max_length=255, null=True)),
                ('blacklist', models.ManyToManyField(related_name='blackmarketer_providers', to='accounts.Provider')),
                ('favorites', models.ManyToManyField(related_name='favmarketer_providers', to='accounts.Provider')),
                ('flag', models.ManyToManyField(related_name='flagmarketer_providers', to='accounts.Provider')),
                ('marketerprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marketer_userprofile', to='accounts.firm')),
            ],
        ),
    ]