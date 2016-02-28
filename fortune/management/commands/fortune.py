"""Give a fortune.
"""
from django.core.management.base import BaseCommand

from ...models import Fortune


class Command(BaseCommand):

    def handle(self, **options):
        print(Fortune.fortune())
