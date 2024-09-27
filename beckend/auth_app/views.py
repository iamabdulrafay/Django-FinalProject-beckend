from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializers,LoginSerializers
from rest_framework.views import APIView
from django.contrib.auth import login

from django.middleware.csrf import get_token
from rest_framework.permissions import AllowAny

class SignupSerializerViewSets(APIView):
    permission_classes = [AllowAny]  

    def post(self,request):
        serializers=SignupSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response({"msg:user create ssuccessfully!"},status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    





from rest_framework.authtoken.models import Token

class LoginSerializerViewSets(APIView):
    permission_classes = [AllowAny]  
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)  # Logs the user in and starts the session
            
            # Generate or get the token for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "msg": "Login successful",
                "token": token.key,  
                "CSRFToken": get_token(request)
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
