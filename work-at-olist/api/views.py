import json
import re

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer

from core.models import Category, Channel


class ChannelsView(viewsets.ReadOnlyModelViewSet):
    """A view for listing channels."""
    queryset = Channel.objects.all()
    serializer_class = None

    def list(self, request):
        """Return a list of channels."""
        q = self.get_queryset().values_list('name', flat=True)
        return Response(list(q))

    def retrieve(self, request, pk=None):
        """Return a list of channels's categories."""
        try:
            channel = Channel.objects.get(name__iexact=pk)
        except:
            raise NotFound
        queryset = Category.objects.filter(channel=channel)
        q = queryset.values_list('name', flat=True)
        return Response(list(q))

    @detail_route(methods=['get', 'post'], url_path='(?P<category>.+)')
    def list_category(self, request, pk=None, category=None):
        """Return a single category and its parents and subcategories."""
        try:
            # Check the requested channel and category exists
            category = re.sub(r'(?<! )/(?! )', ' / ', category)
            channel = Channel.objects.get(name__iexact=pk)
            category = Category.objects.get(channel=channel, name__iexact=category)
        except:
            raise NotFound
        # Find the parent categories name using regex
        parent_name = category.name
        parents_names = []
        while '/' in parent_name:
            parent_name = re.sub(r'(/[^/]+)$',  '', parent_name).strip()
            if parent_name != category.name and parent_name not in parents_names:
                parents_names.append(parent_name)
        parents_names = list(reversed(parents_names))
        # Load subcategories that contain the name of the request category
        # (the requested category in also loaded in this list)
        subcategories = Category.objects.filter(channel=channel, name__istartswith=category.name)
        subcategories_names = subcategories.values_list('name', flat=True)
        # Generate the list of categories to be returned
        categories_list = parents_names + list(subcategories_names)
        return Response(categories_list)
