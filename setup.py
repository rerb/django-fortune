#!/usr/bin/env python
from setuptools import find_packages, setup
import sys


install_requires = ["django>=1.6"]

if sys.version_info[0] == 2:
    install_requires.append("pathlib2")

try:
    import pypandoc
except ImportError:
    print("pypandoc import failed. Long_description conversion failure")
else:
    try:
        long_description = pypandoc.convert("README.md", "rst")
        long_description = long_description.replace("\r", "")
    except OSError:
        print("Pandoc not found. Long_description conversion failure.")
        import io
        # pandoc is not installed, fallback to using raw contents
        with io.open("README.md", encoding="utf-8") as f:
            long_description = f.read()

setup(name="django-fortune",
      version="1.0.1",
      description="A Django template-tag for fortunes.",
      long_description=long_description,
      packages=find_packages(),
      author="Robert Erb",
      author_email="bob.erb@gmail.com",
      license="GPL3",
      keywords="django fortune",
      url="https://github.com/rerb/django-fortune",
      install_requires=install_requires,
      test_suite='runtests.runtests',
      classifiers=[
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Framework :: Django",
          "Development Status :: 5 - Production/Stable"
      ])
