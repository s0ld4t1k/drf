from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.forms import model_to_dict

class WomenAPIView(generics.ListCreateAPIView):
    queryset=Women.objects.all()
    serializer_class=WomenSerializer

class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Women.objects.all()
    serializer_class=WomenSerializer