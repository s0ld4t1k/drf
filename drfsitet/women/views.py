from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.forms import model_to_dict

class WomenAPIView(APIView):
    def get(self,request):
        w=Women.objects.all()
        return Response(WomenSerializer(w,many=True).data)
    
    def post(self,request):
        serializer=WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post=Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response(WomenSerializer(post).data)