# Generated by Django 5.0.6 on 2024-08-12 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_commentmodel_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
