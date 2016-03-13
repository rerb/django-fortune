from rest_framework import serializers
from .models import Fortune, Pack


class FortuneSerializer(serializers.HyperlinkedModelSerializer):
    pack = serializers.HyperlinkedRelatedField(
        many=False,
        view_name="fortune:api:pack-detail",
        read_only=True)
    pack_name = serializers.CharField(max_length=256,
                                      source="pack.name")

    class Meta:
        model = Fortune
        fields = ("id", "text", "pack_name", "pack")


class PackSerializer(serializers.HyperlinkedModelSerializer):
    fortunes = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="fortune:api:fortune-detail",
        read_only=True)

    class Meta:
        model = Pack
        fields = ("id", "name", "fortunes")
