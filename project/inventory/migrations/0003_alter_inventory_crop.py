# Generated by Django 5.1.6 on 2025-04-02 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_added_on_crop_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='inventory.crop'),
        ),
    ]
