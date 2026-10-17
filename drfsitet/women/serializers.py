from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Women
        fields='__all__'
        
