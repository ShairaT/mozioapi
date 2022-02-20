from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Polygon, Point
from mozioApp.serializers import ProviderModelSerializer, ServiceAreaModelSerializer, QueryResponseSerializer
from mozioApp.models import Provider, ServiceArea

# Create your views here.

def index(self):
    base = "<h3> Mozio API</h3>"\
    + '<br>' + '<a href="/provider"> Show all providers </a>'\
    + '<br>' + '<a href="/provider/add"> Add provider </a>'\
    + '<br>' + '<a href="/serviceArea"> Show all Service Areas </a>'\
    + '<br>' + '<a href="/serviceArea/add"> Add service area </a>'\
    + '<br>' + '<a target="_blank" href="https://app.swaggerhub.com/apis/ShairaT/Mozio/1.0.0"> Documentation </a>'
    return HttpResponse(base)

class ProviderAll(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderModelSerializer

class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderModelSerializer

class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderModelSerializer

class ServiceAreaAll(generics.ListAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaModelSerializer

class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaModelSerializer

class ServiceAreaList(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaModelSerializer

@api_view(['GET'])
def query(request):
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)

    if lat is None or lng is None:
        return HttpResponse('Data is incomplete, please add lat and lng. ')

    point = Point(float(lat), float(lng))
    matchPolygons = []
    serviceAreas = ServiceArea.objects.all()
    for area in serviceAreas:
        strPolygon = area.polygon
        print(eval(strPolygon))
        polygon = Polygon(eval(strPolygon))
        if polygon.contains(point):
            matchPolygons.append(area)

    if len(matchPolygons) == 0:
        return Response('No matching data for the given parameters')

    serializer = QueryResponseSerializer(matchPolygons, many=True)
    return Response(serializer.data)
