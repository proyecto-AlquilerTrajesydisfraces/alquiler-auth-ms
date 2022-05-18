from auth_tienda.models.user import User
from rest_framework           import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'password', 'nombre', 'email', 'telefono']


    def to_representation(self, obj):
       #Estructura de datos para devolver la información para
       #cualquier usuario cuando re realiza una petición.
        user    = User.objects.get(id=obj.id)
        return {
            'id'       : user.id,
            'username' : user.username,
            'nombre'   : user.nombre,
            'email'    : user.email,
            'telefono' : user.telefono,
        }