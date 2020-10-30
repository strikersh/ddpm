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
import base64 as b64
import json
import os
import pathlib
import tarfile
import urllib.request as request

# setup and parse command line arguments

parser = argparse.ArgumentParser(description='Install package from DolceSDK packages repository.')

parser.add_argument(
	'package',
	metavar='PACKAGE',
	nargs='+',
	help='Package name or path to local package.')

parser.add_argument(
	'--auth',
	help='username:token for accessing GitHub API')

args = parser.parse_args()

# check DOLCESDK is set

try:
	DOLCESDK = pathlib.Path(os.environ['DOLCESDK']).expanduser()
except KeyError as e:
	sys.exit('Environmental variable DOLCESDK is not set')

INSTALL_PREFIX = DOLCESDK / 'arm-dolce-eabi'
print(f'Installing to {INSTALL_PREFIX}')

# install local packages

network_package = []

for pkg in args.package:
	path = pathlib.Path(pkg)
	if path.is_file():
		with tarfile.open(path) as tar:
			tar.extractall(path=INSTALL_PREFIX)
		print(f'Installed {pkg}')
	else:
		network_package.append(pkg)

if network_package == []:
	sys.exit(0)

# setup request

req = request.Request('https://api.github.com/repos/DolceSDK/packages/releases')

if args.auth:
	username, _ = args.auth.split(':')
	print(f'Authenticating as {username}')
	req.add_header('Authorization', f'Basic {b64.b64encode(args.auth.encode("utf-8")).decode("utf-8")}')

# fetch recent releases

with request.urlopen(req) as res:
	releases = json.loads(res.read().decode('utf-8'))

# find and install package

def install_network_package(pkg):
	for rel in releases:
		for asset in rel['assets']:
			if f'{pkg}.tar.xz'.lower() == asset['name'].lower():
				with request.urlopen(asset['browser_download_url']) as res:
					with tarfile.open(fileobj=res, mode='r|*') as tar:
						tar.extractall(path=INSTALL_PREFIX)
				print(f'Installed {asset["browser_download_url"]}')
				return
	print(f'Cannot find {pkg}')

for pkg in network_package:
	install_network_package(pkg)
