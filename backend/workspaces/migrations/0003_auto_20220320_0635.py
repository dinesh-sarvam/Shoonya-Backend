# Generated by Django 3.1.14 on 2022-03-20 06:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspaces', '0002_auto_20220317_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='manager',
        ),
        migrations.AddField(
            model_name='workspace',
            name='manager',
            field=models.ManyToManyField(null=True, related_name='workspace_manager', to=settings.AUTH_USER_MODEL, verbose_name='manager'),
        ),
    ]
