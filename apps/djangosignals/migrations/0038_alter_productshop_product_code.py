# Generated by Django 4.2.1 on 2023-07-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangosignals', '0037_alter_productshop_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshop',
            name='product_code',
            field=models.BigIntegerField(blank=True, default=8138939175, null=True, unique=True),
        ),
    ]
