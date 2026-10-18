#!/bin/sh
# Builds particles into out/. The compiler and curses library come from the
# environment, so one script serves every target (see
# .github/workflows/release.yml):
#
#   asciiverse/build.sh                                          # Linux, macOS
#   LIBS=-lncursesw LDFLAGS="-static -s" asciiverse/build.sh     # Alpine, static
#   CXX=x86_64-w64-mingw32-g++ CXXFLAGS="-O2 -I$PDC -DPDC_WIDE -DPDC_FORCE_UTF8" \
#     LIBS="$PDC/wincon/pdcurses.a" LDFLAGS="-static -s" EXE=.exe asciiverse/build.sh
set -eu
cd "$(dirname "$0")/.."
CXX="${CXX:-c++}"
CXXFLAGS="${CXXFLAGS:--O2}"
LDFLAGS="${LDFLAGS:-}"
LIBS="${LIBS:--lncurses}"
EXE="${EXE:-}"
mkdir -p out
$CXX $CXXFLAGS -Wall particles.cpp $LDFLAGS $LIBS -o "out/particles$EXE"
echo "built particles$EXE"
