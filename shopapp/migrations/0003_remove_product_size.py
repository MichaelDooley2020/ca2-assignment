# Generated by Django 4.2.6 on 2023-11-30 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product_gender_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]