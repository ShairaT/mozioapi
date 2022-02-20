from rest_framework import serializers
from mozioApp.models import ServiceArea, Provider

class ProviderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class ServiceAreaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceArea
        fields = '__all__'

class QueryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['provider','name', 'price']