from django.conf.urls import url, include
from backend import views as api_views
from rest_framework.authtoken import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'merch', api_views.MerchViewSet)
router.register(r'videos', api_views.VideoViewSet)
router.register(r'releases', api_views.ReleaseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
