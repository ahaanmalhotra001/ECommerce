# Generated by Django 3.1.4 on 2020-12-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201230_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]