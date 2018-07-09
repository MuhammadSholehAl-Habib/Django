from rest_framework import serializers
from .models import marker, siapsat

class markerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = marker
        fields = ('id','url','name','lat','lng','address')

class siapsatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = siapsat
        fields = ('id','url','satuan','latitude','longitude','posisi','kotama')
