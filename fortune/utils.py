import os
import sys

from django.apps import apps

from fortune.models import Pack

if sys.version_info[0] == 2:
    from pathlib2 import Path
else:
    from pathlib import Path


def get_available_pack_names():
    installed_pack_names = [pack.name for pack in Pack.objects.all()]
    fortunes_path = get_fortunes_path()
    for path in fortunes_path.iterdir():
        if path.is_dir():
            pass
        elif path.suffix == ".dat":
            pass
        elif path.name in installed_pack_names:
            pass
        else:
            yield path.name


def get_fortunes_path():
    app_config = apps.get_app_config("fortune")
    return Path(os.sep.join([app_config.path, "fortunes"]))
