# Generated by Django 5.1.6 on 2025-02-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_contact',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
