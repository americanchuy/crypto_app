# Generated by Django 3.2.5 on 2023-04-30 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='ticker',
            field=models.CharField(default='', max_length=8),
        ),
    ]
