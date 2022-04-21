# Generated by Django 3.1.14 on 2022-03-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20220319_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'MonolingualTranslation'), (2, 'TranslationEditing'), (3, 'OCRAnnotation')]),
        ),
    ]