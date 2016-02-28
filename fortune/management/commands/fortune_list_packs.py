"""List available and installed Fortune Packs.
"""
from django.core.management.base import BaseCommand

from ...models import Pack
from ...utils import get_available_pack_names


class Command(BaseCommand):

    def print_installed_packs(self):
        for pack in Pack.objects.all():
            print(pack.name)

    def print_available_packs(self):
        for name in get_available_pack_names():
            print (name)

    def handle(self, *args, **options):
        print("-- Installed: --")
        self.print_installed_packs()
        print("-- Available: --")
        self.print_available_packs()
