from django.db import models


class Channel(models.Model):
    """A model for channels used by sellers to publish their products.

    Attributes:
        name    The name of the channel
    """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        """Return the name of the channel."""
        return self.name


class Category(models.Model):
    """A model for channels' categories of products.

    Attributes:
        name    The name of the category with its path (e.g. Games / XBOX 360 / Console)
    """
    name = models.CharField(max_length=200)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        """Return the name of the category."""
        return self.name
