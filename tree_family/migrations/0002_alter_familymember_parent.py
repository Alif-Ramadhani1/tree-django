# Generated by Django 5.0.6 on 2024-05-14 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_family', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree_family.familymember'),
        ),
    ]
