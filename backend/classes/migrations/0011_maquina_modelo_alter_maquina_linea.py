# Generated by Django 4.1.4 on 2023-01-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0010_alter_maquina_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquina',
            name='modelo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='maquina',
            name='linea',
            field=models.CharField(choices=[('0', 'Ninguna'), ('1', 'Línea 1'), ('2', 'Línea 2'), ('3', 'Línea 3')], default='0', max_length=20),
        ),
    ]