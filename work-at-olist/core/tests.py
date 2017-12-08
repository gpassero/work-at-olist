from django.test import TestCase
from core.models import Channel, Category


class ModelTestCase(TestCase):
    """This class defines the test suite for the channel and category models."""

    def setUp(self):
        """Define the test variables."""
        self.channel_name = "test"
        self.categories_names = [
            'Games / XBOX One',
            'Games / XBOX 360',
            'Games / Playstation 4'
        ]
        self.channel = Channel(name=self.channel_name)
        self.categories = [Category(name=category_name)
                           for category_name in self.categories_names]

    def test_model_can_create_a_channel(self):
        """Test the channel model can create a channel."""
        old_count = Channel.objects.count()
        self.channel.save()
        new_count = Channel.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_categories(self):
        """Test the category model can create a category."""
        self.channel.save()
        old_count = Category.objects.count()
        for category in self.categories:
            category.channel = self.channel
            category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_overwrite_a_channel_categories(self):
        """Test the category model can create a category."""
        self.channel.save()
        old_count = Category.objects.count()
        for category in self.categories:
            category.channel = self.channel
            category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)
        old_count = new_count
        Category.objects.filter(channel=self.channel).delete()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)
