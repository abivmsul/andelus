# Generated by Django 5.0 on 2024-02-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_productgiven_productgivendetail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ordergroup',
            name='approved_by',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
