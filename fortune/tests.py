from django.test import TestCase

from .models import Fortune, Pack


class TestFortune(TestCase):

    def setUp(self):
        self.pack = Pack.objects.create(name="fortunes")

    def test_create_fortune(self):
        """Can we create a fortune?"""
        Fortune.objects.create(text="Good luck for you.",
                               pack=self.pack)

    def test_fortune(self):
        """Does Fortune.fortune() work?"""
        fortunes = ["Good luck for you.",
                    "Good luck for you, too.",
                    "Good luck for you, three."]
        for fortune in fortunes:
            Fortune.objects.create(text=fortune,
                                   pack=self.pack)
        self.assertIn(Fortune.fortune(), fortunes)
