"""offsets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from core import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'developments-geo', views.DevelopmentGeoViewSet, base_name='developments-geo')
router.register(r'developments', views.DevelopmentViewSet)
router.register(r'permit-names', views.PermitNameViewSet)
router.register(r'permits', views.PermitViewSet)
router.register(r'biodiversity-loss', views.BiodiversityLossViewSet)
router.register(r'biodiversity-gain', views.BiodiversityGainViewSet)
router.register(r'implementation-times', views.ImplementationTimeViewSet)
router.register(r'offsets-geo', views.OffsetGeoViewSet, base_name='offsets-geo')
router.register(r'offsets', views.OffsetViewSet)
router.register(r'statistics', views.Statistics, base_name='statistics')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
