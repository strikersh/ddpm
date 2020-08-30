#!/usr/bin/env bash

get_download_link () {
  curl -sL https://raw.githubusercontent.com/DolceSDK/headers/master/.travis.d/last_built_toolchain.py | python3 - $@
}

install_dolcesdk () {
  INSTALLDIR="$1"

  case "$(uname -s)" in
     Darwin*)
      mkdir -p "$INSTALLDIR"
      curl -L "$(get_download_link apple)" | tar xj -C "$INSTALLDIR" --strip-components=1
     ;;

     Linux*)
      mkdir -p "$INSTALLDIR"
      curl -L "$(get_download_link linux)" | tar xj -C "$INSTALLDIR" --strip-components=1
     ;;

     MSYS*|MINGW64*)
      UNIX=false
      mkdir -p "$INSTALLDIR"
      curl -L "$(get_download_link w64)" | tar xj -C "$INSTALLDIR" --strip-components=1
     ;;

     CYGWIN*|MINGW32*)
      echo "Please use msys2. Exiting..."
      exit 1
     ;;

     *)
       echo "Unknown OS"
       exit 1
      ;;
  esac

}
