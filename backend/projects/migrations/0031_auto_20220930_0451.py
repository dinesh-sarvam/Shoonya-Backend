# Generated by Django 3.2.14 on 2022-09-30 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0030_auto_20220901_0835"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_type",
            field=models.CharField(
                choices=[
                    ("MonolingualTranslation", "MonolingualTranslation"),
                    ("TranslationEditing", "TranslationEditing"),
                    (
                        "SemanticTextualSimilarity_Scale5",
                        "SemanticTextualSimilarity_Scale5",
                    ),
                    ("ContextualTranslationEditing", "ContextualTranslationEditing"),
                    ("OCRAnnotation", "OCRAnnotation"),
                    ("MonolingualCollection", "MonolingualCollection"),
                    ("SentenceSplitting", "SentenceSplitting"),
                    (
                        "ContextualSentenceVerification",
                        "ContextualSentenceVerification",
                    ),
                    ("ConversationTranslation", "ConversationTranslation"),
                    (
                        "ConversationTranslationEditing",
                        "ConversationTranslationEditing",
                    ),
                ],
                help_text="Project Type indicating the annotation task",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="projecttaskrequestlock",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
