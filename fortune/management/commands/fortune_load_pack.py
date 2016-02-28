"""Load a Fortune Pack.
"""
import sys

from django.core.management.base import BaseCommand

from ...models import Pack
from ...utils import get_available_pack_names, get_fortunes_path

if sys.version_info[0] == 2:
    FileNotFoundError = IOError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("pack_name")

    def handle(self, *args, **options):
        try:
            Pack.objects.get(name=options["pack_name"])
        except Pack.DoesNotExist:
            pass
        else:
            print(options["pack_name"], " is already loaded")
            return
        fortunes_path = get_fortunes_path()
        pack_filename = str(fortunes_path.joinpath(options["pack_name"]))
        try:
            Pack.load(pack_filename)
        except FileNotFoundError:
            print(options["pack_name"], "is not a valid Pack name")
            print("available packs:", " ".join(get_available_pack_names()))
            return
