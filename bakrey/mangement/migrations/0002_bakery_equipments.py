# Generated by Django 3.2.3 on 2021-06-19 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bakery_Equipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipment_name', models.CharField(max_length=100)),
                ('Equipment_type', models.CharField(max_length=100)),
                ('Equipment_Quanity', models.CharField(max_length=100)),
                ('entry_date_time', models.DateField()),
            ],
        ),
    ]
