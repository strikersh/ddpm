#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -z "$DOLCESDK" ]; then
  echo '$DOLCESDK is not set'
  exit 1
fi

. "$DIR/include/install-packages.sh"

echo "==> Updating packages"
install_packages

echo "All done!"
