# Generated by Django 5.0.2 on 2024-02-24 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_order_price_alter_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
