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
import platform
import tarfile
import urllib.request as request

# setup and parse command line arguments (no arguments)

argparse.ArgumentParser(description='Install DolceSDK.').parse_args()

# check DOLCESDK is set

try:
	DOLCESDK = pathlib.Path(os.environ['DOLCESDK'])
except KeyError as e:
	sys.exit('Environmental variable DOLCESDK is not set')

print(f'Installing to {DOLCESDK}')

# check machine architecture

mach = platform.machine()

if mach.lower() in ['x86_64', 'amd64']:
	mach = 'x86_64'
else:
	sys.exit(f'Unsupported machine architecture {mach}')

print(f'Detected machine architecture {mach}')

# check operating system

plat = platform.system()

if plat.lower().startswith('linux'):
	plat = 'linux-gnu'
elif plat.lower().startswith('darwin'):
	plat = 'apple-darwin'
elif plat.lower().startswith('windows') or plat.lower().startswith('msys'):
	plat = 'w64-mingw32'
else:
	sys.exit(f'Unsupported platform {plat}')

print(f'Detected platform {plat}')

# fetch recent releases

with request.urlopen('https://api.github.com/repos/DolceSDK/autobuilds/releases') as res:
	releases = json.loads(res.read().decode('utf-8'))

# install SDK

for rel in releases:
	for asset in rel['assets']:
		if asset['name'].startswith(f'dolcesdk-{mach}-{plat}-'):
			print(f'Installing {asset["browser_download_url"]}')
			DOLCESDK.mkdir(parents=True, exist_ok=True)
			with request.urlopen(asset['browser_download_url']) as res:
				with tarfile.open(fileobj=res, mode='r|*') as tar:
					for f in tar:
						f.name = f.name[len('dolcesdk/'):]
						tar.extract(f, path=DOLCESDK)
						print(f'Installed {DOLCESDK / f.name}')
			sys.exit(0)

sys.exit('Cannot find SDK release.')
