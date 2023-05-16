# Generated by Django 4.1 on 2023-05-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosetta_example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='definition_en',
            field=models.TextField(blank=True, null=True, verbose_name='definition'),
        ),
        migrations.AddField(
            model_name='words',
            name='definition_ru',
            field=models.TextField(blank=True, null=True, verbose_name='definition'),
        ),
        migrations.AddField(
            model_name='words',
            name='definition_uz',
            field=models.TextField(blank=True, null=True, verbose_name='definition'),
        ),
        migrations.AddField(
            model_name='words',
            name='word_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='word'),
        ),
        migrations.AddField(
            model_name='words',
            name='word_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='word'),
        ),
        migrations.AddField(
            model_name='words',
            name='word_uz',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='word'),
        ),
        migrations.AlterField(
            model_name='words',
            name='language',
            field=models.CharField(blank=True, default='en', max_length=10),
        ),
    ]
