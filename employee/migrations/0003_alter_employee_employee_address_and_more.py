# Generated by Django 5.1.3 on 2025-02-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_employeemodel_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_contact',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
