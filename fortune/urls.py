from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"fortunes", views.FortuneViewSet)
router.register(r"packs", views.PackViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls",
                               namespace="rest_framework")),
]
