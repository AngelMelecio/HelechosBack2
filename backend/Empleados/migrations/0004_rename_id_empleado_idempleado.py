# Generated by Django 4.1.4 on 2022-12-25 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0003_alter_empleado_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='id',
            new_name='idEmpleado',
        ),
    ]
