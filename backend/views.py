from django.shortcuts import render
from rest_framework import viewsets
from backend.models import Merch, Release, Video
from backend.serializers import MerchSerializer, ReleaseSerializer, VideoSerializer
from rest_framework import permissions
import django_filters.rest_framework

class MerchViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('merch_id',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReleaseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('release_id',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Create your views here.
