from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from core.models import Channel, Category


class ViewTestCase(APITestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test variables."""
        self.channel = Channel(name='test_channel')
        self.channel.save()
        self.categories_names = [
            'Games',
            'Games / XBOX One',
            'Games / XBOX One / Console',
            'Games / XBOX One / Acessories',
            'Games / XBOX One / Games',
            'Games / XBOX 360',
            'Games / Playstation 4',
            'Books',
            'Books / National Literature',
            'Books / National Literature / Science Fiction',
            'Books / National Literature / Fiction Fantastic',
            'Books / Foreign Language',
        ]
        self.categories = [Category(name=name, channel=self.channel)
                           for name in self.categories_names]
        for category in self.categories:
            category.save()
        self.responses = {
            'list_channels': self.client.get('/channels/'),
            'list_channel_categories': self.client.get('/channels/%s/' % self.channel.name),
            'list_category_relcategories': self.client.get('/channels/%s/%s' % (self.channel.name, self.categories_names[1]))
        }

    def test_api_can_list_channels(self):
        """Test the api can list channels."""
        response = self.responses['list_channels']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response.data, {'name': self.channel.name})

    def test_api_can_list_channel_categories(self):
        """Test the api can list a channel's categories."""
        response = self.responses['list_channel_categories']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response.data, {'name': self.categories_names[0]})

    def test_api_can_list_category_relcategories(self):
        """Test the api can return a category with parent and subcategories."""
        response = self.responses['list_category_relcategories']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response.data, {'name': self.categories_names[0]})
        self.assertContains(response.data, {'name': self.categories_names[2]})
