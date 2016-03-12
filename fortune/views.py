from .models import Fortune, Pack
from .serializers import FortuneSerializer, PackSerializer
from rest_framework import renderers, viewsets
from rest_framework.decorators import detail_route


class FortuneViewSet(viewsets.ModelViewSet):
    queryset = Fortune.objects.all()
    serializer_class = FortuneSerializer


class PackViewSet(viewsets.ModelViewSet):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def load(self, request, *args, **kwargs):
        raise NotImplementedError

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def unload(self, request, *args, **kwargs):
        raise NotImplementedError
