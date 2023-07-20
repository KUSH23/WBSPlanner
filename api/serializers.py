from rest_framework import serializers
from .models import MGroup, MSGroup

class MGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MGroup
        fields = '__all__'
        # fields = ['mgroup_name', 'slug', 'description']


class MSGroupSerializer(serializers.ModelSerializer):
    mgroup_name = MGroupSerializer()
    class Meta:
        model = MSGroup
        fields = '__all__'