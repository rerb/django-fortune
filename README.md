[![Travis](https://img.shields.io/travis/rerb/django-fortune.svg)](https://travis-ci.org/rerb/django-fortune)
[![Codecov](https://img.shields.io/codecov/c/github/rerb/django-fortune.svg)]()
[![PyPI](https://img.shields.io/pypi/v/django-fortune.svg)]()
[![PyPI](https://img.shields.io/pypi/pyversions/django-fortune.svg)]()
[![PyPI](https://img.shields.io/pypi/status/django-fortune.svg)]()

# django-fortune
A Django template-tag that provides a fortune.

## The Template Tag

```html
{% fortune %}
```

## The Management Commands

```bash
$ python manage.py fortune  # Get a fortune. 
Fortunes will improve after loading some.  # Oops, no fortunes loaded.
$ python manage.py fortune_list_packs  # List available fortune packs.
-- Installed: --
-- Available: --
art
ascii-art
computers
cookie
definitions
.
.
$ python manage.py fortune_load_pack art  # Load art fortunes.
$ python manage.py fortune  # Get an art fortune.

"My life is a soap opera, but who has the rights?"
        -- Madame
$ python manage.py fortune_unload_pack art  # Unload art fortunes.
$ python manage.py fortune  # No fortunes available again. :-(
Fortunes will improve after loading some.
$
```

## The Python Interface

```python
$ python manage.py shell
.
.
>>> from fortune.models import Fortune, Pack
>>> Fortune.fortune()
'Fortunes will improve after loading some.'
>>> from fortune import utils
>>> fortunes_path = utils.get_fortunes_path()
>>> art_fortunes_path = fortunes.path.joinpath("art")
>>> Pack.load(str(art_fortunes_path))
>>> Fortune.fortune()
u"\nThey can't stop us... we're on a mission from God!\n\t\t-- The Blues Brother"
>>> art_fortunes = Pack.objects.get(name="art".title())
>>> art_fortunes.unload()
>>> Fortune.fortune()
'Fortunes will improve after loading some.'
>>>
```

## Installation

Install using pip;
```bash
$ pip install django-fortune
```

then add "fortune" to INSTALLED_APPS in your app's settings.py.

