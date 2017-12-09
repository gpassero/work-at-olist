from rest_framework import serializers

from core.models import Channel, Category


class FKSerializer(serializers.Serializer):
    """Serialize an entity's uuid and name."""
    uuid = serializers.UUIDField()
    name = serializers.CharField(max_length=200)


class ChannelCategorySerializer(serializers.ModelSerializer):
    """Serialize a category with its related categories and channel."""
    parent = serializers.UUIDField(source='parent.uuid', read_only=True)

    class Meta:
        model = Category
        editable = False
        fields = ('uuid', 'name', 'parent')


class ChannelSerializer(serializers.ModelSerializer):
    """Serialize a channel and its categories."""
    categories = ChannelCategorySerializer(many=True)

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
