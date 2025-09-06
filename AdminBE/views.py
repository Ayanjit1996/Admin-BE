from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

# Serializer for login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data['username']
    return Response({"message": f"Login successful for {username}"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def dashboard(request):
    return Response({"message": "Welcome to dashboard"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def profile(request):
    return Response({"username": "ayanjit", "bio": "Hello, I’m here!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def settings(request):
    return Response({"theme": "dark", "notifications": True}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    return Response({"message": "You have been logged out"}, status=status.HTTP_200_OK)
