# Generated by Django 4.1 on 2023-05-16 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosetta_example', '0002_words_definition_en_words_definition_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='words',
            name='definition_en',
        ),
        migrations.RemoveField(
            model_name='words',
            name='definition_ru',
        ),
        migrations.RemoveField(
            model_name='words',
            name='definition_uz',
        ),
        migrations.RemoveField(
            model_name='words',
            name='word_en',
        ),
        migrations.RemoveField(
            model_name='words',
            name='word_ru',
        ),
        migrations.RemoveField(
            model_name='words',
            name='word_uz',
        ),
    ]
