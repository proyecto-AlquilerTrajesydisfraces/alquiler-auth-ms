from rest_framework                         import status, views
from rest_framework.response                import Response
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer
from auth_tienda.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        #request.data es lo que esta llegando en el body
        serializer = UserSerializer(data=request.data)
        #is valid va a verificar que los campos que colocamos en field, esten llegando en el cuerpo de la petición 
        serializer.is_valid(raise_exception=True)
        serializer.save()

        token_data       = {"username":request.data['username'],
                            "password":request.data['password']}
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)