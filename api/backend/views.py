import random
import requests
import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from http import HTTPStatus
from django.shortcuts import get_object_or_404

from .models import Service
from .serializers import ServiceSerializer, ResultSerializer




class History(APIView):
    def get(self, request):
        print(requests.get('http://127.0.0.1:8000/api/v1/testserver'))
        model = Service.objects.all()
        serializer = ServiceSerializer(model, many=True)
        return Response(serializer.data)


class TestServer(APIView):
    def get(self, request):
        status = random.choice([False, True])
        return Response({"status": status})


class Ping(APIView):
    def get(self, request):
        response = requests.get('http://127.0.0.1:8000/api/v1/testserver')
        result = {}
        if response.status_code == HTTPStatus.OK:
            result['status'] = 'Работает'
        else:
            result['status'] = 'Не работает'
        return Response(result)


class Query(APIView):
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            response = requests.get('http://127.0.0.1:8000/api/v1/testserver')
            time.sleep(10)
            jsons = response.json()
            validated_data['status'] = str(jsons['status'])
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Result(APIView):
    def get(self, request, id):
        model = Service.objects.filter(cadastral_number=id)
        serializer = ResultSerializer(model, many=True)
        return Response(serializer.data)