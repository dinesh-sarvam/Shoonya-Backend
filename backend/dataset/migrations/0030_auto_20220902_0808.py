# Generated by Django 3.1.14 on 2022-09-02 08:08

from django.db import migrations, models

def add_default_organization_id_where_null(apps, schema_editor):
    from dataset.models import DatasetInstance
    from organizations.models import Organization

    DatasetInstance.objects.filter(organisation_id__isnull=True).update(
        organisation_id=Organization.objects.get(pk=1)
    )

def add_default_speaker_count_where_null(apps, schema_editor):
    from dataset.models import Conversation

    Conversation.objects.filter(speaker_count__isnull=True).update(
        speaker_count=2
    )

class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0029_auto_20220901_0844'),
        ("dataset", "0028_auto_20220617_1309"),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='conversation_json',
            field=models.JSONField(help_text='Details of the conversation', verbose_name='conversation_details'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='speaker_count',
            field=models.IntegerField(help_text='Number of speakers involved in conversation', verbose_name='speaker_count'),
        ),
        migrations.RunPython(add_default_speaker_count_where_null),
        migrations.RunPython(add_default_organization_id_where_null),
    ]
