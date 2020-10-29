#!/usr/bin/env bash

set -e

if [ -n "$AUTH" ]; then
	AUTH="--auth $AUTH"
fi

# test installation
python3 dolcesdk-update.py $AUTH
python3 dolcesdk-update-packages.py $AUTH

# test installation overwrite
python3 dolcesdk-update.py $AUTH
python3 dolcesdk-update-packages.py $AUTH

# test ddpm
python3 ddpm.py $AUTH zlib
python3 ddpm.py $AUTH zlib bzip2

# test cmake
cmake . -D CMAKE_INSTALL_PREFIX="$DOLCESDK"
make install
