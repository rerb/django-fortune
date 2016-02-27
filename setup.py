import os
from setuptools import find_packages, setup


setup(name="django-fortune",
      version="0.1",
      description="A Django template-tag for fortunes.",
      long_description=open(os.path.join(os.path.dirname(__file__),
                                         "README.md")).read(),
      packages=find_packages(),
      author="Robert Erb",
      author_email="bob.erb@gmail.com",
      license="GPL3",
      keywords="django fortune",
      url="https://github.com/rerb/django-fortune",
      install_requires=["django>=1.3"],
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
          "Framework :: Django"
      ])
