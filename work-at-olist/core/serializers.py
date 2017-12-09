from rest_framework import serializers

from core.models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):
    """Serialize a channel and its categories."""
    class Meta:
        model = Channel
        editable = False
        fields = ('name', 'categories')


class EntityNameSerializer(serializers.Serializer):
    """Serialize an entity's name."""
    name = serializers.CharField(max_length=200)


class CategorySerializer(serializers.ModelSerializer):
    """Serialize a category with its related categories and channel."""
    channel = EntityNameSerializer()
    parent = EntityNameSerializer()
    subcategories = EntityNameSerializer(many=True)

    class Meta:
        model = Category
        editable = False
        fields = ('name', 'channel', 'parent', 'subcategories')
