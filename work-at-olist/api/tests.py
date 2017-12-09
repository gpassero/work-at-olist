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
        self.categories_tree = {
            'Games': {
                'XBOX One': ['Console', 'Acessories', 'Games'],
                'XBOX 360': None,
                'Playstation 4': None
            },
            'Books': {
                'National Literature': ['Science Fiction', 'Fiction Fantastic'],
                'Foreign Language': None
            }
        }
        self.categories = []
        self.create_categories_recursive(self.categories_tree)
        self.responses = {
            'list_channels': self.client.get('/channels/'),
            'list_channel_categories': self.client.get('/channels/%s/' % self.channel.uuid),
            'list_category_relcategories': self.client.get('/categories/%s/' % (self.categories[1].uuid))
        }

    def create_categories_recursive(self, categories, parent=None):
        for name in categories:
            category = Category(name=name, parent=parent, channel=self.channel)
            category.save()
            self.categories.append(category)
            if isinstance(categories, dict):
                subcategories = categories[name]
                if subcategories:
                    self.create_categories_recursive(subcategories, category)

    def test_api_can_list_channels(self):
        """Test the api can list channels."""
        response = self.responses['list_channels']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.channel.name)

    def test_api_can_list_channel_categories(self):
        """Test the api can list a channel's categories."""
        response = self.responses['list_channel_categories']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.categories[0].name)

    def test_api_can_list_category_relcategories(self):
        """Test the api can return a category with parent and subcategories."""
        response = self.responses['list_category_relcategories']
        self.assertContains(response, self.categories[0].name)
        self.assertContains(response, self.categories[2].name)
