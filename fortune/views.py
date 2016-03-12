from .models import Fortune, Pack
from .serializers import FortuneSerializer, PackSerializer
from rest_framework import renderers, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


class FortuneViewSet(viewsets.ModelViewSet):
    queryset = Fortune.objects.all()
    serializer_class = FortuneSerializer

    @list_route(methods=["get"])
    def random(self, request):
        fortune = Fortune.random_fortune()
        serializer = self.get_serializer(fortune)
        return Response(serializer.data)


class PackViewSet(viewsets.ModelViewSet):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def load(self, request, *args, **kwargs):
        raise NotImplementedError

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def unload(self, request, *args, **kwargs):
        raise NotImplementedError
