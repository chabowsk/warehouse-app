# Generated by Django 5.1.4 on 2024-12-31 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_inventory_status_sold_item_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='stored_at',
        ),
    ]