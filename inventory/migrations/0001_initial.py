# Generated by Django 4.2 on 2023-04-09 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invetory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_inbound_price', models.IntegerField()),
                ('total_outbound_price', models.IntegerField()),
                ('total_inbound_quantity', models.IntegerField()),
                ('total_outbound_quantity', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
    ]
