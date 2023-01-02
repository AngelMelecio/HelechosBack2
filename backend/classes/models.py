from django.db import models


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.


class Empleado(models.Model):
    idEmpleado = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=200, null=True, blank=True)
    ns = models.CharField(max_length=16)
    usuario = models.CharField(max_length=200, null=True, blank=True)
    contrasena = models.CharField(max_length=200, null=True, blank=True)
    fotografia = models.ImageField(
        upload_to=upload_to, max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=20,
                                    choices=[('Trabajador', 'Trabajador'),('Encargado', 'Encargado'),('Administrador', 'Administrador')],
                                    default='Trabajador')
    departamento = models.CharField(max_length=20,
                            choices=[('Tejido', 'Tejido'),('Corte', 'Corte'),('Plancha', 'Plancha'),
                                    ('Empaque', 'Empaque'),('Transporte', 'Transporte'),('Diseno', 'Diseño'),('Gerencia', 'Gerencia')],
                            default='Tejido' )

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)


class Maquina(models.Model):
    idMaquina = models.AutoField(auto_created=True, primary_key=True)
    numero = models.CharField(max_length=50)
    linea = models.CharField(max_length=20,
                            choices=[('0', 'Ninguna'),('1', 'Línea 1'),('2', 'Línea 2'),('3', 'Línea 3')],
                            default='0')
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    ns = models.CharField(max_length=60)
    fechaAdquisicion = models.DateField()
    otros = models.TextField(null=True, blank=True)
    departamento = models.CharField(max_length=20,
                            choices=[('Tejido', 'Tejido'),('Corte', 'Corte'),('Plancha', 'Plancha'),
                                    ('Empaque', 'Empaque'),('Transporte', 'Transporte'),('Diseno', 'Diseño'),('Gerencia', 'Gerencia')],
                            default='Tejido')


class Cliente(models.Model):
    idCliente = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=200)
    otro = models.DateField()
    fotografia = models.CharField(max_length=225)


class Contacto(models.Model):
    idContacto = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=200)
    puesto = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    idCliente = models.CharField(max_length=20)


class Modelo(models.Model):
    idModelo = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=200)
    colores = models.CharField(max_length=200)
    fichaTecnica = models.FileField(null=True, blank=True)


class Pedido(models.Model):

    idPedido = models.AutoField(auto_created=True, primary_key=True)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idModelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    fechaActual = models.DateTimeField()
    fechaEntrega = models.DateTimeField()
    proveedores = models.CharField(max_length=200)


class DetallePedido(models.Model):
    idDetallePedido = models.AutoField(auto_created=True, primary_key=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    talla = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)


class Reposicion(models.Model):
    idReposicion = models.AutoField(auto_created=True, primary_key=True)
    fecha = models.DateTimeField()
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    idMaquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    idEmpleadoRepuso = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='%(class)s_empleado_repuso')
    idEmpleadoRevisor = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='%(class)s_empleado_revisor')
    cantidad = models.CharField(max_length=50)


class EmpleadoMaquina(models.Model):
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    idMaquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)


class Produccion(models.Model):
    idProduccion = models.AutoField(auto_created=True, primary_key=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    idDetallePedido = models.ForeignKey(
        DetallePedido, on_delete=models.CASCADE)
    idEtiqueta = models.CharField(max_length=20)
    tejido = models.BooleanField()
    fechaTejido = models.DateTimeField()
    idEmpleadoTejedor = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='%(class)s_empleado_tejedor')
    idMaquinaTejido = models.ForeignKey(
        Maquina,
        on_delete=models.CASCADE,
        related_name='%(class)s_maquina_tejido')
    plancha = models.BooleanField()
    fechaPlancha = models.DateTimeField()
    idEmpleadoPlanchador = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='%(class)s_empleado_planchador')
    idMaquinaPlancha = models.ForeignKey(
        Maquina,
        on_delete=models.CASCADE,
        related_name='%(class)s_maquina_plancha')
    corte = models.BooleanField()
    fechaCorte = models.DateTimeField()
    idEmpleadoCortador = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='%(class)s_empleado_cortador')
    idMaquinaCorte = models.ForeignKey(
        Maquina,
        on_delete=models.CASCADE,
        related_name='%(class)s_maquina_corte')
    empaque = models.BooleanField()
    fechaEmpaque = models.DateTimeField()
    idEmpleadoEmpacador = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='%(class)s_empleado_empacador')
    salida = models.BooleanField()
    fechaSalida = models.DateTimeField()
    idEmpleadoRepartidor = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='%(class)s_empleado_repartidor')
    numSemana = models.CharField(max_length=20)
