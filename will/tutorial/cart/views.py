from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from rest_framework import viewsets
from .serializers import CartSerializers

from .models import Cart

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('title')
    serializer_class = CartSerializers
