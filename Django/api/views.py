from django.shortcuts import render

from api.models import Empresa
from rest_framework import viewsets
from api.serializers import EmpresaSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


@api_view(['POST'])
def soma_view(request, numero1, numero2):
    total = numero1 + numero2
    return Response({"resultado": total}, status=status.HTTP_200_OK)
