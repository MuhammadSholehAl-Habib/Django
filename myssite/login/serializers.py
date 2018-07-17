from rest_framework import serializers
from .models import marker, siapsat, organization, ekko

class markerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = marker
        fields = ('id','url','name','lat','lng','address')

class siapsatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = siapsat
        fields = ('id','url','satuan','latitude','longitude','posisi','kotama')

class organizationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = organization
        fields = ('id','url','name','level')

class ekkoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ekko
        fields = ('id','url','mantap','satuan_id')
