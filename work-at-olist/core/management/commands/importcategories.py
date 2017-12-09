from os.path import isfile

from django.core.management.base import BaseCommand, CommandError

from core.models import Category, Channel


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
        categories_paths = []
        created_categories = []
        with open(categories_filename, 'rt', encoding='utf8') as inp:
            # TODO Check the parent category is in the db if its not found in created_categories
            # (may happen if the file is not sorted)
            for line in inp:
                category_path = line.strip().replace('\n', '')
                if category_path != '':
                    categories_paths.append(category_path)
                    last_slash_pos = category_path.rfind('/')
                    parent = None
                    parent_path = ''
                    parent_name = ''
                    if last_slash_pos != -1:
                        parent_path = category_path[:last_slash_pos].strip()
                        parent_last_slash_pos = parent_path.rfind('/')
                        parent_name = parent_path[parent_last_slash_pos + 1:].strip()
                        for created_category in reversed(created_categories):
                            if created_category.name == parent_name:
                                parent = created_category
                                break
                        if not parent:
                            self.stderr.write('Could not find the parent of category %s (check the file is sorted).' %
                                              category_path)
                    category_name = category_path[last_slash_pos + 1:].strip()
                    self.stdout.write('Creating category %s...' % category_path)
                    category = Category(name=category_name, channel=channel, parent=parent)
                    category.save()
                    created_categories.append(category)
        n_categories = len(created_categories)
        self.stdout.write('Channel %s was imported with %i categories.' % (channel_name, n_categories))
