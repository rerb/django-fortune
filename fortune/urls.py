from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"fortunes", views.FortuneViewSet)
router.register(r"packs", views.PackViewSet)

urlpatterns = [
    url(r"^api/",
        include(router.urls,
                namespace="api"))
]
