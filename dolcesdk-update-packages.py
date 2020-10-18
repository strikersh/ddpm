#!/usr/bin/env python3

'''
This file is part of DolceSDK
Copyright (C) 2020 Reiko Asakura

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import sys

if sys.version_info < (3, 6):
	sys.exit('Python must be at least version 3.6')

import argparse
import json
import os
import pathlib
import tarfile
import urllib.request as request

# setup and parse command line arguments (no arguments)

parser = argparse.ArgumentParser(description='Install all packages from DolceSDK packages repository.').parse_args()

# check DOLCESDK is set

try:
	DOLCESDK = pathlib.Path(os.environ['DOLCESDK'])
except KeyError as e:
	sys.exit('Environmental variable DOLCESDK is not set')

INSTALL_PREFIX = DOLCESDK / 'arm-dolce-eabi'
print(f'Installing to {INSTALL_PREFIX}')

# fetch recent releases

with request.urlopen('https://api.github.com/repos/DolceSDK/packages/releases') as res:
	releases = json.loads(res.read().decode('utf-8'))

# install package

for asset in releases[0]['assets']:
	with request.urlopen(asset['browser_download_url']) as res:
		with tarfile.open(fileobj=res, mode='r|*') as tar:
			tar.extractall(path=INSTALL_PREFIX)
	print(f'Installed {asset["browser_download_url"]}')
