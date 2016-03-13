import os

from django.db import models, transaction
from django.db.utils import IntegrityError


def filename_to_pack_name(filename):
    return os.path.splitext(
        os.path.basename(filename))[0].title().replace("_", " ")


class PackAlreadyLoadedError(Exception):
    pass


class Pack(models.Model):

    name = models.CharField(max_length=256,
                            unique=True)

    @classmethod
    def load(cls, pack_filename, pack_name=None):
        pack_name = (pack_name or filename_to_pack_name(pack_filename))
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
