# Generated by Django 4.1.4 on 2022-12-25 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_rename_id_empleado_idempleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=200)),
                ('otro', models.DateField()),
                ('fotografia', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idContacto', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('puesto', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('idCliente', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('idDetallePedido', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('talla', models.CharField(max_length=50)),
                ('cantidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('idMaquina', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=50)),
                ('linea', models.CharField(max_length=4)),
                ('marca', models.CharField(max_length=60)),
                ('ns', models.CharField(max_length=60)),
                ('fechaAdquisicion', models.DateField()),
                ('otros', models.CharField(max_length=200)),
                ('departamento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('idModelo', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('colores', models.CharField(max_length=200)),
                ('fichaTecnica', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPedido', models.CharField(max_length=20)),
                ('fechaActual', models.DateTimeField()),
                ('fechaEntrega', models.DateTimeField()),
                ('proveedores', models.CharField(max_length=200)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.cliente')),
                ('idModelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Reposicion',
            fields=[
                ('idReposicion', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('cantidad', models.CharField(max_length=50)),
                ('idEmpleadoRepuso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_empleado_repuso', to='classes.empleado')),
                ('idEmpleadoRevisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_empleado_revisor', to='classes.empleado')),
                ('idMaquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.maquina')),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('idProduccion', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idEtiqueta', models.CharField(max_length=20)),
                ('tejido', models.BooleanField()),
                ('fechaTejido', models.DateTimeField()),
                ('plancha', models.BooleanField()),
                ('fechaPlancha', models.DateTimeField()),
                ('corte', models.BooleanField()),
                ('fechaCorte', models.DateTimeField()),
                ('empaque', models.BooleanField()),
                ('fechaEmpaque', models.DateTimeField()),
                ('salida', models.BooleanField()),
                ('fechaSalida', models.DateTimeField()),
                ('numSemana', models.CharField(max_length=20)),
                ('idDetallePedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.detallepedido')),
                ('idEmpleadoCortador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_empleado_cortador', to='classes.empleado')),
                ('idEmpleadoEmpacador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_empleado_empacador', to='classes.empleado')),
                ('idEmpleadoPlanchador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_empleado_planchador', to='classes.empleado')),
                ('idEmpleadoRepartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_empleado_repartidor', to='classes.empleado')),
                ('idEmpleadoTejedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_empleado_tejedor', to='classes.empleado')),
                ('idMaquinaCorte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_maquina_corte', to='classes.maquina')),
                ('idMaquinaPlancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_maquina_plancha', to='classes.maquina')),
                ('idMaquinaTejido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_maquina_tejido', to='classes.maquina')),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoMaquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.empleado')),
                ('idMaquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.maquina')),
            ],
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='idPedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.pedido'),
        ),
    ]
