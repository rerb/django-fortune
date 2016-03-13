from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .models import (Fortune,
                     Pack,
                     PackAlreadyLoadedError,
                     UnavailablePackError,
                     get_available_pack_names)
from .serializers import FortuneSerializer, PackSerializer


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

    @list_route(methods=["get"])
    def loaded(self, request, *args, **kwargs):
        """Return a list of loaded Packs.
        """
        serializer = self.get_serializer(list(Pack.objects.all()),
                                         many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def available(self, request, *args, **kwargs):
        """Return a list of available (unloaded) Pack names.
        """
        packs = []
        for pack_name in get_available_pack_names():
            packs.append(pack_name)
        return Response(packs)

    @list_route(methods=["post"])
    def load(self, request, *args, **kwargs):
        try:
            name = request.data["name"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            Pack.load(pack_name=name)
        except UnavailablePackError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except PackAlreadyLoadedError:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_201_CREATED)

    @detail_route(methods=["post"])
    def unload(self, request, *args, **kwargs):
        name = request.data.get("name", None)
        pack = get_object_or_404(Pack, name=name)
        pack.unload()
        return Response(status=status.HTTP_204_NO_CONTENT)
