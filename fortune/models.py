import os
import sys

from django.db import models, transaction


def filename_to_pack_name(filename):
    return os.path.splitext(
        os.path.basename(filename))[0].title().replace("_", " ")


class Pack(models.Model):

    name = models.CharField(max_length=256,
                            unique=True)

    @classmethod
    def load(cls, pack_filename, pack_name=None):
        pack_name = (pack_name or filename_to_pack_name(pack_filename))

        with transaction.atomic():
            pack = cls.objects.create(name=pack_name)
            with open(pack_filename, 'r') as pack_file:
                fortunes = pack_file.read()
                for fortune in [f[:-1] for f in fortunes.split('\n%')]:
                    if fortune:  # No empty fortunes.
                        Fortune.objects.create(text=fortune, pack=pack)

    def unload(self, pack_filename=sys.stdout):
        with open(pack_filename, 'w') as pack_file:
            for fortune in Fortune.objects.filter(pack=self):
                pack_file.write(fortune.text + '\n%\n')
        self.delete()


class Fortune(models.Model):

    text = models.CharField(max_length=2046,
                            unique=True)
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text

    @classmethod
    def fortune(cls):
        fortune = cls.objects.order_by("?").first()
        if fortune:
            return fortune.text
        else:
            return "Fortunes will improve after loading some."
