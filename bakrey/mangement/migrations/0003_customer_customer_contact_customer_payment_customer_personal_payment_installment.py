# Generated by Django 3.2.3 on 2021-06-19 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mangement', '0002_bakery_equipments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_first_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_payment', models.IntegerField()),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.customer')),
            ],
        ),
        migrations.CreateModel(
            name='payment_installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recieve_amount', models.IntegerField()),
                ('remaining_amount', models.IntegerField()),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.customer_payment')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_CNIC', models.IntegerField()),
                ('Customer_DOB', models.DateField()),
                ('Customer_age', models.IntegerField()),
                ('Customer_House_Number', models.IntegerField()),
                ('Customer_Street', models.CharField(max_length=50)),
                ('Customer_Town', models.CharField(max_length=50)),
                ('Customer_City', models.IntegerField()),
                ('Customer_Country', models.CharField(max_length=50)),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Contact_Number', models.CharField(max_length=50)),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.customer')),
            ],
        ),
    ]