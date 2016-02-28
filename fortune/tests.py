import os
import tempfile

from django.test import TestCase

from .models import (Fortune,
                     Pack,
                     filename_to_pack_name)


class FilenameToPackNameTestCase(TestCase):

    def test_long_path(self):
        """Does filename_to_pack_name handle a long path?"""
        full_path = "/Favorites/chvrches/EveryOpenEye/never_ending_circles.mp3"
        self.assertEqual("Never Ending Circles",
                         filename_to_pack_name(full_path))


class PackTestCase(TestCase):

    fortunes = ["Good luck for everybody.",
                "Good luck for me.",
                "Good luck for you."]
    pack_data = "\n%\n".join(fortunes) + "\n%\n"

    def test_load(self):
        """Can we load a Pack of Fortunes from a file?"""
        pack_file = tempfile.NamedTemporaryFile(mode="w",
                                                delete=False)
        pack_file.write(self.pack_data)
        pack_file.close()
        try:
            Pack.load(pack_file.name)
        except:
            raise
        finally:
            os.remove(pack_file.name)
        self.assertEqual(3, Fortune.objects.count())

    def test_load_named_pack(self):
        """Can we load a Pack and name it?"""
        pack_file = tempfile.NamedTemporaryFile(mode="w",
                                                delete=False)
        pack_file.write(self.pack_data)
        pack_file.close()
        try:
            Pack.load(pack_file.name, pack_name="Test Fortunes")
        except:
            raise
        finally:
            os.remove(pack_file.name)
        pack = Pack.objects.first()
        self.assertEqual("Test Fortunes", pack.name)

    def test_unload(self):
        """Can we unload a Pack of Fortunes?"""
        pack = Pack.objects.create(name="Test Pack")
        for fortune in self.fortunes:
            Fortune.objects.create(text=fortune, pack=pack)
        pack_file = tempfile.NamedTemporaryFile(mode="w")
        pack.unload(pack_filename=pack_file.name)
        self.assertEqual(0, Pack.objects.count())

    def test_unload_removes_fortunes(self):
        """When we unload a Pack of Fortunes, do the Fortunes go away?"""
        pack = Pack.objects.create(name="Test Pack")
        for fortune in self.fortunes:
            Fortune.objects.create(text=fortune, pack=pack)
        pack_file = tempfile.NamedTemporaryFile(mode="w")
        pack.unload(pack_filename=pack_file.name)
        self.assertEqual(0, Fortune.objects.count())

    def test_unload_output(self):
        """When we unload a Pack of Fortunes, are they saved into a file?"""
        pack = Pack.objects.create(name="Test Pack")
        for fortune in self.fortunes:
            Fortune.objects.create(text=fortune, pack=pack)
        pack_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
        pack_filename = pack_file.name
        try:
            pack.unload(pack_filename=pack_file.name)
            pack_file.close()
            pack_file = open(pack_filename, 'r')
            lines = pack_file.read()
        except:
            raise
        finally:
            pack_file.close()
            os.remove(pack_file.name)
        self.assertEqual(self.pack_data, lines)


class FortuneTestCase(TestCase):

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
