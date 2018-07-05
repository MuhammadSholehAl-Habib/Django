from rest_framework import serializers
from .models import marker

class markerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = marker
        fields = ('id','url','name','lat','lng','address')
