# Generated by Django 4.2.1 on 2023-05-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangosignals', '0017_alter_productshop_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshop',
            name='product_code',
            field=models.BigIntegerField(blank=True, default=9468540937, null=True, unique=True),
        ),
    ]
