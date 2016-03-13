"""Unload a Fortune Pack.
"""
from django.core.management.base import BaseCommand

from ...models import Pack


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("pack_name")

    def handle(self, **options):
        try:
            pack = Pack.objects.get(name=options["pack_name"].title())
        except Pack.DoesNotExist:
            print("fortune.models.DoesNotExist: Pack with name {name} "
                  "is not loaded".format(name=options["pack_name"]))
            print("loaded Packs: " + " ".join([pack.name for pack in
                                              Pack.objects.all()]))
            return
        pack.unload()
