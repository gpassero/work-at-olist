from rest_framework import serializers

from core.models import Channel, Category


class EntityNameSerializer(serializers.Serializer):
    """Serialize an entity's name."""
    name = serializers.CharField(max_length=200)


class FKSerializer(serializers.Serializer):
    """Serialize an entity's uuid and name."""
    uuid = serializers.UUIDField()
    name = serializers.CharField(max_length=200)


class ChannelSerializer(serializers.ModelSerializer):
    """Serialize a channel and its categories."""
    class Meta:
        model = Channel
        editable = False
        fields = ('uuid', 'name', 'categories')


class CategorySerializer(serializers.ModelSerializer):
    """Serialize a category with its related categories and channel."""
    channel = FKSerializer()
    parent = FKSerializer()
    subcategories = FKSerializer(many=True)

    class Meta:
        model = Category
        editable = False
        fields = ('uuid', 'name', 'channel', 'parent', 'subcategories')
