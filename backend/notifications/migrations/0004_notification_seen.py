# Generated by Django 3.2.14 on 2023-12-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notifications", "0003_auto_20231122_2154"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="seen",
            field=models.BooleanField(default=False),
        ),
    ]
