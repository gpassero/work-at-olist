import uuid

from django.db import models


class Channel(models.Model):
    """A model for channels used by sellers to publish their products.

    Attributes:
        uuid        Unique identifier for the channel
        name        The name of the channel
        categories  The categories of the channel
    """
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        """Return the name of the channel."""
        return 'Channel %s - %s' % (self.uuid, self.name)


class Category(models.Model):
    """A model for channels' categories of products.

    Attributes:
        uuid            Unique identifier for the category
        name            The name of the category
        parent          The parent category
        channel         The parent channel
        subcategories   The subcategories of the channel
    """
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='subcategories')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        unique_together = ('name', 'parent')

    def __str__(self):
        """Return the name of the category."""
        return 'Category %s - %s' % (self.uuid, self.name)
