# Generated by Django 3.1.4 on 2020-12-31 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cartproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='products.CartProduct'),
        ),
    ]