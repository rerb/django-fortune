#!/usr/bin/env python
from setuptools import find_packages, setup
import sys


def readme():
    with open('README.rst') as f:
        return f.read()

install_requires = ["django>=1.6"]

if sys.version_info[0] == 2:
    install_requires.append("pathlib2")

setup(name="django-fortune",
      version="1.0.6",
      description="A Django template-tag for fortunes.",
      long_description=readme(),
      packages=find_packages(),
      include_package_data=True,
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
