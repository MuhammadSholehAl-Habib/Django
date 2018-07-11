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
        fields = ('id','url','name','level','priority_type','combat_type','is_induk','is_rahwan','parent_id','level_0_id','latitude','longitude','img_path','leader','vice_leader')

class ekkoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ekko
        fields = ('id','url','personnel_quantity','personnel_quality','personnel_mantap','personnel_status','materiil_quantity','materiil_quality','materiil_mantap','materiil_status','exercise_quantity','exercise_quality','exercise_mantap','exercise_status','pangkalan_quantity','pangkalan_quality','pangkalan_mantap','pangkalan_status','penak_quantity','penak_quality','penak_mantap','penak_status','quantity','quality','mantap','status','induk','periode','year','satuan_id')
