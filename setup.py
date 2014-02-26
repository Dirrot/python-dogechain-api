#!/usr/bin/env python2

from distutils.core import setup
from os.path import abspath
from os.path import join as path_join
from os import getcwd
from shutil import rmtree

import DogechainApi

pathname		=		getcwd()

packages        =       ['DogechainApi']

setup(name		    =		'DogechainApi',
      version		=		'0.0.1',
      description	=		'Python API for www.dogechain.info',
      author		=		'Dirrot',
      author_email  =       'dirrot@web.de',
      url		    =		'https://github.com/Dirrot/python-dogechain-api',
      packages		=		packages,
      package_dir	=		{'DogechainApi.py' : abspath(path_join(pathname, 'DogechainApi/'))},
      data_files	=		[('share/DogechainApi', ['README.md', 'LICENSE', 'img/donation-qr-code.png'])],

	)


try:
	rmtree(abspath(path_join(pathname, 'build/')))
except:
	pass
