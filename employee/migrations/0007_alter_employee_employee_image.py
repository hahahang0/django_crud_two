# Generated by Django 5.1.3 on 2025-02-18 15:38

import employee.validators_files.fileValidators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_employee_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_image',
            field=models.FileField(blank=True, null=True, upload_to='employee_profile_image/', validators=[employee.validators_files.fileValidators.file_size]),
        ),
    ]
