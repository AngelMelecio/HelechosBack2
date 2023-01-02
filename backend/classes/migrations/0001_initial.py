# Generated by Django 4.1.4 on 2022-12-21 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.CharField(blank=True, max_length=200, null=True)),
                ('ns', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=200)),
                ('contrasena', models.CharField(max_length=200)),
                ('fotografia', models.CharField(blank=True, max_length=255, null=True)),
                ('departamento', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
    ]
