from django.shortcuts import render
from rest_framework import viewsets
from backend.models import Merch, Release, Video
from backend.serializers import MerchSerializer, ReleaseSerializer, VideoSerializer
from rest_framework import permissions

class MerchViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReleaseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Create your views here.
