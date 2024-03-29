# Generated by Django 5.0 on 2024-02-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_issued_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subunit',
            field=models.CharField(blank=True, choices=[('liter', 'Liter'), ('kg', 'Kilogram'), ('packets', 'Packets'), ('piece', 'Piece')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='subunit_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='with_tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='unit',
            field=models.CharField(choices=[('liter', 'Liter'), ('kg', 'Kilogram'), ('packets', 'Packets'), ('piece', 'Piece')], max_length=20),
        ),
    ]
