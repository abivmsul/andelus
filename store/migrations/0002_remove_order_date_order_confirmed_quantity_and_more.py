# Generated by Django 5.0 on 2024-01-06 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='confirmed_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ordergroup',
            name='approved_by',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordergroup',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]