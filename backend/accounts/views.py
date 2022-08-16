from .models import Address
from .serializers import AddressSerializer, RegisterUserSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# Create your views here.


@csrf_exempt
@api_view(['POST'])
def register(request):
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=201)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(
        instance=request.user)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=200)


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
