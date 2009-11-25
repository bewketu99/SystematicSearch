##############################################################################
#
# Copyright (c) 2008 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

__version__ = '1.2unreleased'

import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.txt')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires=[
    'setuptools',
    'Chameleon',
    'sourcecodegen>=0.6.11', # tests fail without this requirement?  (wtf)
    'Paste > 1.7', # temp version pin to prevent PyPi install failure :-(
    'PasteDeploy',
    'PasteScript',
    'WebOb',
    'zope.interface >= 3.5.1',  # 3.5.0 comment: "allow to bootstrap on jython"
    'zope.component >= 3.6.0', # independent of zope.hookable
    'zope.configuration',
    'zope.deprecation',
    'repoze.lru',
    ]

if sys.version_info[:2] < (2, 6):
    install_requires.append('simplejson')
    
setup(name='repoze.bfg',
      version=__version__,
      description='A WSGI web framework influenced by Zope, Django, and Pylons',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: BFG",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
        ],
      keywords='web wsgi bfg zope',
      author="Agendaless Consulting",
      author_email="repoze-dev@lists.repoze.org",
      url="http://bfg.repoze.org",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages = ['repoze', 'repoze.bfg'],
      zip_safe=False,
      install_requires = install_requires,
      tests_require= install_requires + ['Sphinx', 'docutils', 'coverage'],
      test_suite="repoze.bfg.tests",
      entry_points = """\
        [paste.paster_create_template]
        bfg_starter=repoze.bfg.paster:StarterProjectTemplate
        bfg_zodb=repoze.bfg.paster:ZODBProjectTemplate
        bfg_routesalchemy=repoze.bfg.paster:RoutesAlchemyProjectTemplate
        bfg_alchemy=repoze.bfg.paster:AlchemyProjectTemplate
        [paste.paster_command]
        bfgshell=repoze.bfg.paster:BFGShellCommand
      """
      )

