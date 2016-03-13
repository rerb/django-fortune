import os
import sys

from django.apps import apps
from django.db import models, transaction
from django.db.utils import IntegrityError

if sys.version_info[0] == 2:
    from pathlib2 import Path
else:
    from pathlib import Path


def filename_to_pack_name(filename):
    return os.path.splitext(
        os.path.basename(filename))[0].title().replace("_", " ")


def get_available_pack_names():
    """Return a list of (lower-cased) names if available (unloaded) Packs.
    """
    installed_pack_names = [pack.name.lower() for pack in Pack.objects.all()]
    fortunes_path = get_fortunes_path()
    for path in fortunes_path.iterdir():
        if path.is_dir():
            pass
        elif path.suffix == ".dat":
            pass
        elif path.name.lower() in installed_pack_names:
            pass
        else:
            yield path.name.lower()


def get_fortunes_path():
    """Return the path to the fortunes data packs.
    """
    app_config = apps.get_app_config("fortune")
    return Path(os.sep.join([app_config.path, "fortunes"]))


class PackAlreadyLoadedError(Exception):
    pass


class UnavailablePackError(Exception):
    pass


class Pack(models.Model):

    name = models.CharField(max_length=256,
                            unique=True)

    @classmethod
    def load(cls, pack_name):
        if pack_name.lower() not in get_available_pack_names():
            raise UnavailablePackError
        fortunes_path = get_fortunes_path()
        pack_filename = str(fortunes_path.joinpath(pack_name))
        with transaction.atomic():
            try:
                pack = cls.objects.create(name=pack_name)
            except IntegrityError:
                raise PackAlreadyLoadedError
            with open(pack_filename, 'r') as pack_file:
                fortunes = pack_file.read()
                for fortune in [f[:-1] for f in fortunes.split('\n%')]:
                    if fortune:  # No empty fortunes.
                        Fortune.objects.create(text=fortune, pack=pack)

    def unload(self):
        self.delete()


class Fortune(models.Model):

    text = models.CharField(max_length=2046)
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE,
                             related_name="fortunes")

    class Meta:
        unique_together = ('pack', 'text')

    def __unicode__(self):
        return self.text

    @classmethod
    def random_fortune(cls):
        fortune = cls.objects.order_by("?").first()
        return fortune

    @classmethod
    def fortune(cls):
        fortune = cls.random_fortune()
        if fortune:
            return fortune.text
        else:
            return "Fortunes will improve after loading some."
