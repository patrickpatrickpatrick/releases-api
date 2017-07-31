from rest_framework import serializers
from backend.models import Merch, Release, Video
from django.contrib.auth.models import User

class MerchSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Merch
        fields = ('id', 'name', 'url', 'stock', 'item', 'price','owner',)

class ReleaseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Release
        fields = ('id', 'name', 'artist', 'url', 'embed', 'release_number', 'medium', 'release_id','description','owner',)

class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Video
        fields = ('id', 'name', 'artist', 'embed','owner',)

class UserSerializer(serializers.ModelSerializer):
    merch = serializers.PrimaryKeyRelatedField(many=True, queryset=Merch.objects.all())
    releases = serializers.PrimaryKeyRelatedField(many=True, queryset=Release.objects.all())
    videos = serializers.PrimaryKeyRelatedField(many=True, queryset=Video.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'merch', 'releases', 'videos')