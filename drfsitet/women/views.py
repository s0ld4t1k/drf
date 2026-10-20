from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.decorators import action
from rest_framework.permissions import *

class WomenViewSet(viewsets.ModelViewSet):
    # queryset=Women.objects.all()
    serializer_class=WomenSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pk=self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    @action(methods=['get'],detail=True)
    def category(self,request,pk=None):
        cats=Category.objects.get(pk=pk)
        return Response({'cats':cats.name})

class WomenAPIList(generics.ListCreateAPIView):
    queryset=Women.objects.all()
    serializer_class=WomenSerializer
    # permission_classes=(IsAuthenticatedOrReadOnly,)

class WomenAPIDetail(generics.RetrieveUpdateAPIView):
    queryset=Women.objects.all()
    serializer_class=WomenSerializer
    permission_classes=(IsOwnerOrReadOnly,)

class WomenAPIDelete(generics.RetrieveDestroyAPIView):
    queryset=Women.objects.all()
    serializer_class=WomenSerializer
    permission_classes=(IsAdminUser,)