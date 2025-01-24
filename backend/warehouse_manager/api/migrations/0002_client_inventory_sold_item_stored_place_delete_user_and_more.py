# Generated by Django 5.1.4 on 2024-12-31 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('OEM_number', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sold_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Stored_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rack', models.CharField(max_length=5)),
                ('shelf', models.CharField(max_length=5)),
                ('case', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='inventory',
            name='stored_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stored_place'),
        ),
    ]
