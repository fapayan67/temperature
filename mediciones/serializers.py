from rest_framework import serializers

from .models import Area, Region, Measurements

class AreaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Area
        # para mostrar solo los especificos de mis modelos
        #fields = ['id''name','owner']
        fields = '__all__'

class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class MeasurementsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'