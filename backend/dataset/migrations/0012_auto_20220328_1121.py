# Generated by Django 3.1.14 on 2022-03-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0011_ocrdocument_prediction_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentencetext',
            name='is_profane',
            field=models.BooleanField(default=False),
        ),
    ]
