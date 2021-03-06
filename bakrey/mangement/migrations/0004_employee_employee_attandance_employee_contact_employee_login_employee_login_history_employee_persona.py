# Generated by Django 3.2.3 on 2021-06-19 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mangement', '0003_customer_customer_contact_customer_payment_customer_personal_payment_installment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_First_Name', models.CharField(max_length=50)),
                ('Employee_Last_Name', models.CharField(max_length=50)),
                ('Employee_Email', models.EmailField(max_length=254)),
                ('Employee_Type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Professional_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Experince', models.CharField(max_length=50)),
                ('Job_description', models.CharField(max_length=50)),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill_Name', models.CharField(max_length=50)),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee_professional_details')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salary_Ammount', models.IntegerField()),
                ('Advance_Salary', models.IntegerField()),
                ('Paid', models.IntegerField()),
                ('Remaining', models.IntegerField()),
                ('Salary_Date', models.DateField()),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Previous_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Previous_job', models.CharField(max_length=50)),
                ('Previous_job_duration', models.CharField(max_length=50)),
                ('Previous_job_Company', models.CharField(max_length=50)),
                ('Reason_to_left_old_job', models.CharField(max_length=50)),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_CNIC', models.CharField(max_length=50)),
                ('Employee_DOB', models.DateField()),
                ('Employee_Age', models.CharField(max_length=50)),
                ('Employee_Education', models.CharField(max_length=100)),
                ('Employee_Can_Drive', models.CharField(max_length=20)),
                ('Employee_House_Number', models.CharField(max_length=50)),
                ('Employee_Street', models.CharField(max_length=50)),
                ('Employee_Town', models.CharField(max_length=50)),
                ('Employee_City', models.CharField(max_length=50)),
                ('Employee_Country', models.CharField(max_length=60)),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_login_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Password', models.CharField(max_length=50)),
                ('Employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Contact_Numeber', models.CharField(max_length=50)),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee_personal')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangement.employee')),
            ],
        ),
    ]
