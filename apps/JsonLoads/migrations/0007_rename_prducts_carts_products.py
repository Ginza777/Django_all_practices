# Generated by Django 4.2.1 on 2023-07-14 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JsonLoads', '0006_remove_carts_id_carts_cart_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carts',
            old_name='prducts',
            new_name='products',
        ),
    ]
