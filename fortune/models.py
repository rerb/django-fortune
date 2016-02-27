from django.db import models


class Pack(models.Model):

    name = models.CharField(max_length=256,
                            unique=True)


class Fortune(models.Model):

    text = models.CharField(max_length=2046,
                            unique=True)
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text

    @classmethod
    def fortune(self):
        fortune = Fortune.objects.order_by("?").first()
        if fortune:
            return fortune.text
        else:
            return "Fortunes will improve after loading some."
