from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='nocoast',
      version=version,
      description="Python package for nocoast work",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='whit',
      author_email='whit at nocoast.us',
      url='http://nocoast.us',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'PasteDeploy',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = nocoast.wsgiapp:make_app
      """,
      )
