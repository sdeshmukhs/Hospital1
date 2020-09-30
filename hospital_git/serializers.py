from rest_framework import serializers
from . models import Doctors


class DoctorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    specialization = serializers.CharField(max_length=50)
    degree = serializers.CharField(max_length=50)
    api_url = serializers.SerializerMethodField('get_api_url')

    class Meta:
        model = Doctors
        fields = ('name','specialization')