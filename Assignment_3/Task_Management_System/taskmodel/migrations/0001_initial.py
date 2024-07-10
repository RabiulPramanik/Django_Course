# Generated by Django 5.0.6 on 2024-07-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('decription', models.TextField()),
                ('is_complete', models.BooleanField(default=False)),
                ('assing_date', models.DateTimeField()),
            ],
        ),
    ]
