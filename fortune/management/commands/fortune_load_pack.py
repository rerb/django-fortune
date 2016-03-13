"""Load a Fortune Pack.
"""
from django.core.management.base import BaseCommand

from ...models import Pack


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("pack_name")

    def handle(self, *args, **options):
        Pack.load(options["pack_name"])
