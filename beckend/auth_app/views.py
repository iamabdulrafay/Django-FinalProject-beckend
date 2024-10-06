from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializers, LoginSerializers
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.permissions import AllowAny

class SignupSerializerViewSets(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializers = SignupSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg": "User created successfully!"}, status=status.HTTP_201_CREATED)
        
        print(serializers.errors)  # Debugging line
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginSerializerViewSets(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"msg": "Login successful"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
