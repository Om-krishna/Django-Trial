from model import greetings
from rest_framework import serializers
class greetingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = greetings
        fields = ('hii', 'hello')