# Generated by Django 5.1.3 on 2025-02-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_employee_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
