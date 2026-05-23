from django.shortcuts import render

from api.models import Empresa
from rest_framework import viewsets
from api.serializers import EmpresaSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


@api_view(['POST'])
def soma_view(request, numero1, numero2):
    total = numero1 + numero2
    return Response({"resultado": total}, status=status.HTTP_200_OK)

@api_view(['POST'])
def soma_formato2(request):
    # Pegando os valores do JSON enviado na requisição
    numero1 = request.data.get('numero1')
    numero2 = request.data.get('numero2')

    total = numero1 + numero2
    return Response({"resultado": total}, status=status.HTTP_200_OK)



class SomaFormato2View(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["numero1", "numero2"],
            properties={
                "numero1": openapi.Schema(type=openapi.TYPE_INTEGER, description="Primeiro número inteiro"),
                "numero2": openapi.Schema(type=openapi.TYPE_INTEGER, description="Segundo número inteiro"),
            },
        ),
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"resultado": openapi.Schema(type=openapi.TYPE_INTEGER)}
        )},
    )
    def post(self, request):
        numero1 = request.data.get('numero1')
        numero2 = request.data.get('numero2')
        total = int(numero1) + int(numero2)
        return Response({"resultado": total}, status=status.HTTP_200_OK)
