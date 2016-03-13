from django.test import TestCase

from ..models import (Fortune,
                      Pack,
                      filename_to_pack_name,
                      get_available_pack_names)


FORTUNES = ["Good luck for everybody.",
            "Good luck for me.",
            "Good luck for you."]
PACK_DATA = "\n%\n".join(FORTUNES) + "\n%\n"


class FilenameToPackNameTestCase(TestCase):

    def test_long_path(self):
        """Does filename_to_pack_name handle a long path?
        """
        full_path = "/Favorites/chvrches/EveryOpenEye/never_ending_circles.mp3"
        self.assertEqual("Never Ending Circles",
                         filename_to_pack_name(full_path))


class GetAvailablePackNamesTestCase(TestCase):

    def test(self):
        """Does get_available_pack_names work?
        """
        self.assertIn("art", list(get_available_pack_names()))

    def test_loaded_packs_are_not_listed(self):
        """Are loaded Packs listed as available?
        """
        Pack.objects.create(name="Art")
        self.assertNotIn("art", list(get_available_pack_names()))


class PackTestCase(TestCase):

    def test_load(self):
        """Can we load a Pack of Fortunes?
        """
        Pack.load("art")
        self.assertEqual(1, Pack.objects.count())

    def test_unload(self):
        """Can we unload a Pack of Fortunes?
        """
        pack = Pack.objects.create(name="Test Pack")
        for fortune in FORTUNES:
            Fortune.objects.create(text=fortune, pack=pack)
        pack.unload()
        self.assertEqual(0, Pack.objects.count())

    def test_unload_removes_fortunes(self):
        """When we unload a Pack of Fortunes, do the Fortunes go away?
        """
        pack = Pack.objects.create(name="Test Pack")
        for fortune in FORTUNES:
            Fortune.objects.create(text=fortune, pack=pack)
        pack.unload()
        self.assertEqual(0, Fortune.objects.count())


class FortuneTestCase(TestCase):

    def setUp(self):
        self.pack = Pack.objects.create(name="fortunes")

    def test_fortune(self):
        """Does Fortune.fortune() work?
        """
        fortunes = ["Good luck for you.",
                    "Good luck for you, too.",
                    "Good luck for you, three."]
        for fortune in fortunes:
            Fortune.objects.create(text=fortune,
                                   pack=self.pack)
        self.assertIn(Fortune.fortune(), fortunes)
