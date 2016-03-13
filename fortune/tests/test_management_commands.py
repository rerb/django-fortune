from django.core.management import call_command
from django.test import TestCase


from ..models import Pack, UnavailablePackError


class ManagementCommandsTestCase(TestCase):

    def test_fortune_load_pack(self):
        """Does fortune_load_pack work?
        """
        args = ["art"]
        opts = {}
        call_command("fortune_load_pack", *args, **opts)
        self.assertEqual(1, Pack.objects.count())

    def test_fortune_load_pack_bad_pack_name(self):
        """Does fortune_load_pack act reasonable when a bad pack name is given?
        """
        args = ["asdf"]
        opts = {}
        with self.assertRaises(UnavailablePackError):
            call_command("fortune_load_pack", *args, **opts)
