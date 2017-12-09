from django.test import TestCase
from core.models import Channel, Category


class ModelTestCase(TestCase):
    """Test suite for the channel and category models."""

    def setUp(self):
        """Define the test variables."""
        self.channel_name = "test"
        self.category_name = 'Games'
        self.subcategories_names = [
            'XBOX One',
            'XBOX 360',
            'Playstation 4'
        ]
        self.channel = Channel(name=self.channel_name)
        self.category = Category(name=self.category_name)
        self.subcategories = [Category(name=category_name)
                              for category_name in self.subcategories_names]

    def test_model_can_create_a_channel(self):
        """Test the channel model can create a channel."""
        old_count = Channel.objects.count()
        self.channel.save()
        new_count = Channel.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_categories(self):
        """Test the category model can create a category."""
        self.channel.save()
        self.category.channel = self.channel
        self.category.save()
        old_count = Category.objects.count()
        for category in self.subcategories:
            category.parent = self.category
            category.channel = self.channel
            category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_overwrite_a_channel_categories(self):
        """Test the category model can create a category."""
        self.channel.save()
        self.category.channel = self.channel
        self.category.save()
        old_count = Category.objects.count()
        for category in self.subcategories:
            category.parent = self.category
            category.channel = self.channel
            category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)
        old_count = new_count
        Category.objects.filter(channel=self.channel).delete()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)
