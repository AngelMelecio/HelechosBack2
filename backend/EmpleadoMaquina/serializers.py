from rest_framework import serializers
 
# import the todo data model
from classes.models import EmpleadoMaquina, Empleado, Maquina
 
# create a serializer class
class EmpleadoMaquinaSerializer(serializers.ModelSerializer):
    

    # create a meta class
    class Meta:
        model = EmpleadoMaquina
        fields = '__all__'