# Generated by Django 5.0.6 on 2024-08-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_brandmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
