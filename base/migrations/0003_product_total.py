# Generated by Django 4.2 on 2023-04-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
