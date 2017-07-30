from django.shortcuts import render
from rest_framework import viewsets
from backend.models import Merch, Release, Video
from backend.serializers import MerchSerializer, ReleaseSerializer, VideoSerializer

class MerchViewSet(viewsets.ModelViewSet):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer

class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

# Create your views here.
