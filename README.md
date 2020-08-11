Dolcedev Package manager
========================

DDPM is a project which aims on getting common libraries building for the PS Vita using the
[DolceSDK toolchain](https://github.com/DolceSDK). It was based off the original idea of xerpi's
vita\_portlibs.


Usage
=====

Getting started
---------------

**You should make sure you have the `curl` command installed.**

### Mac & Linux
First install cmake, you can get this from [Homebrew](http://brew.sh) on Mac (`brew install cmake`),
and from your distro's package manager on Linux (on ubuntu: `sudo apt-get install cmake`).

```shell
git clone https://github.com/DolceSDK/ddpm
cd ddpm
./bootstrap-dolcesdk.sh
export DOLCESDK=/usr/local/dolcesdk # define $DOLCESDK if you haven't already
export PATH=$DOLCESDK/bin:$PATH # add DolceSDK tool to $PATH if you haven't already
./install-all.sh
```

### Windows (Bash on Ubuntu on Windows)

Just follow the steps for Linux above. This is the recommended way to set up ddpm on Windows, however, it only works for Windows 10.

Read here for information on how to install Bash on Ubuntu on Windows: https://msdn.microsoft.com/en-us/commandline/wsl/install_guide

### Windows (msys2)

For older versions of Windows, you should use msys2. Get it from here: https://msys2.github.io/. Only 64-bit version is supported.

```shell
# Read through https://msys2.github.io/ and make sure your msys2 is up-to-date first
pacman -S make git curl p7zip tar cmake
git clone https://github.com/DolceSDK/ddpm
cd ddpm
./bootstrap-dolcesdk.sh
export DOLCESDK=/usr/local/dolcesdk # define $DOLCESDK if you haven't already
export PATH=$DOLCESDK/bin:$PATH # add DolceSDK tool to $PATH if you haven't already
./install-all.sh
```

Update/reinstall
----------------

Run `./dolcesdk-update` which will replace files in `$DOLCESDK` with the latest nightly and libraries.


Contributing
============

Contributions are welcome to both the package repo, documentation or the package manager itself.

License
-------
LGPL v2.1 or later.
