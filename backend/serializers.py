from rest_framework import serializers
from backend.models import Merch, Release, Video

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = ('id', 'name', 'url', 'stock', 'item', 'price',)

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ('id', 'name', 'artist', 'url', 'embed', 'release_number', 'medium', 'release_id','description',)

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'name', 'artist', 'embed',)
