# Generated by Django 5.1.3 on 2025-02-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=200)),
                ('employee_email', models.EmailField(max_length=254)),
                ('employee_contact', models.CharField(max_length=20, unique=True)),
                ('employee_address', models.CharField(max_length=200)),
            ],
        ),
    ]
