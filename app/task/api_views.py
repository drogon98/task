from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from django.contrib.auth import get_user_model,authenticate
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import permissions,status


from .serializers import UserSerializer



class SignInView(APIView):

    permission_classes = (permissions.AllowAny,)

    authentication_classes = ()

    def post(self,request,format=None):
        
        data = request.data

        primary = data.get("primary")

        user = None

        if self.check_is_email(primary):
            user = authenticate(email=primary,password=data.get("password"))
        else:
            user = authenticate(phone=primary,password=data.get("password"))

        if not user:
            return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

        token = user.encode_auth_token(user.id)

        serialized_user = UserSerializer(user)

        return Response({
            'user': serialized_user.data,           
            'token': token.decode(),
        },status=status.HTTP_200_OK)




    

    def check_is_email(self,e):
        if "@" in e:
            return True
        return False