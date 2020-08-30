#!/usr/bin/env bash
#
# DolceSDK package manager
#

set -e
set -o errtrace

error() {
  echo ""
  echo "Failed to install, the package probably does not exist."
  exit 1
}

install_pkg() {
  echo "Installing $1..."
  if [ -f $1 ]; then
    tar -C "$DOLCESDK/arm-dolce-eabi" -Jxvf "$1"
  else
    curl -sL "https://bin.shotatoshounenwachigau.moe/dolcesdk/packages/$1.tar.xz" | tar -C "$DOLCESDK/arm-dolce-eabi" -Jxvf -
  fi
  echo "success"
}

if [ "$#" -ne 1 ]; then
    echo "Usage: ./ddpm package-name"
    exit 1
fi

if [ -z "$DOLCESDK" ]; then
  echo '$DOLCESDK is not set'
  exit 1
fi

trap 'error' ERR
install_pkg "$1"
