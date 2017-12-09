import re

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer

from core.models import Channel, Category
from core.serializers import ChannelSerializer, CategorySerializer, EntityNameSerializer


class ChannelsView(viewsets.ReadOnlyModelViewSet):
    """A view for listing channels and its categories."""
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def list(self, request):
        """Return a list of channels."""
        serializer = EntityNameSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Return a list of channels's categories."""
        try:
            channel = Channel.objects.get(name__iexact=pk)
        except:
            raise NotFound
        queryset = Category.objects.filter(channel=channel)
        serializer = EntityNameSerializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get', 'post'], url_path='(?P<category>.+)')
    def list_category(self, request, pk=None, category=None):
        """Return a single category and its parents and subcategories."""
        try:
            # Check the requested channel and category exists
            channel = Channel.objects.get(name__iexact=pk)
            queryset = Category.objects.filter(channel=channel, name__iexact=category)
        except:
            raise NotFound
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

