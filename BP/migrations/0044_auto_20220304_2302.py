# Generated by Django 3.2.11 on 2022-03-04 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0043_remove_doc_document_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='document',
        ),
        migrations.AddField(
            model_name='treatmentnote',
            name='document',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treatmentnote_doc', to='BP.doc'),
        ),
    ]