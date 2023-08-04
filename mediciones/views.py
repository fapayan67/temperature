from django.shortcuts import render
from rest_framework import generics
from .models import Area, Region, Measurements
from .serializers import AreaSerializers, RegionSerializers, MeasurementsSerializers
# Create your views here.

class AreaAPILisView(generics.ListAPIView):
    serializer_class=AreaSerializers
    queryset = Area.objects.all()

class AreaAPICreateView(generics.CreateAPIView):
    serializer_class=AreaSerializers
    queryset = Area.objects.all()

class RegionAPILisView(generics.ListAPIView):
    serializer_class=RegionSerializers
    queryset = Region.objects.all()

class MeasurementsAPILisView(generics.ListAPIView):
    serializer_class=MeasurementsSerializers
    queryset = Measurements.objects.all()

class MeasurementsAPICreateView(generics.CreateAPIView):
    serializer_class=MeasurementsSerializers
    queryset = Measurements.objects.all()