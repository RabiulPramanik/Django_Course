# Generated by Django 5.0.6 on 2024-07-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taskmodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('taskmodel', models.ManyToManyField(to='taskmodel.taskmodel')),
            ],
        ),
    ]
