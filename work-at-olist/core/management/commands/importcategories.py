from django.core.management.base import BaseCommand, CommandError
from core.models import Channel, Category
from os.path import isfile


class Command(BaseCommand):
    help = 'Import a channels\' categories from a text file.'

    def add_arguments(self, parser):
        parser.add_argument('channel_name', type=str,
                            help='The name of the channel to be created (or overwritten).')
        parser.add_argument('categories_filename', type=str,
                            help='The path to a text file with a list of categories (one for each line).')

    def handle(self, channel_name, categories_filename, *args, **options):
        if not isfile(categories_filename):
            raise CommandError('The specified filename does not exist.')
        try:
            channel = Channel.objects.get(name=channel_name)
            self.stdout.write('Overwriting channel %s...' % channel_name)
            Category.objects.filter(channel=channel).delete()
        except Channel.DoesNotExist:
            self.stdout.write('Creating channel %s...' % channel_name)
            channel = Channel(name=channel_name)
            channel.save()
        with open(categories_filename, 'rt', encoding='utf8') as inp:
            for line in inp:
                category_name = line.strip().replace('\n', '')
                if category_name == '':
                    continue
                self.stdout.write('Creating category %s...' % category_name)
                category = Category(name=category_name, channel=channel)
                category.save()
        self.stdout.write('Categories import finished.')
