import re

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.exceptions import NotFound, APIException
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer

from core.models import Channel, Category
from core.serializers import ChannelSerializer, CategorySerializer, FKSerializer


class ChannelsView(viewsets.ReadOnlyModelViewSet):
    """A view for listing channels and its categories."""
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def list(self, request):
        """Return a list of channels."""
        serializer = FKSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Return a single channel and its categories."""
        try:
            channel = Channel.objects.get(uuid=pk)
        except:
            raise NotFound
        serializer = ChannelSerializer(channel)
        return Response(serializer.data)


class CategoriesView(viewsets.ReadOnlyModelViewSet):
    """A view for listing categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        raise APIException('Can\'t list all categories. Check /channels/<channel-uuid> to see a list of categories of a channel.')

    def retrieve(self, request, pk=None):
        """Return a single category and its parents and subcategories."""
        try:
            category = Category.objects.get(uuid=pk)
        except:
            raise NotFound
        serializer = CategorySerializer(category)
        return Response(serializer.data)
