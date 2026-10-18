#!/bin/sh
# Packs the build into dist/particles-<target>.tar.gz (.zip for Windows) for
# av: the binary at the top beside README, LICENSE, NOTICE and PATCHES.md.
#
#   asciiverse/package.sh x86_64-unknown-linux-musl
set -eu
cd "$(dirname "$0")/.."
target="$1"
case "$target" in *windows*) exe=.exe ;; *) exe= ;; esac
stage=stage/particles
rm -rf "$stage" && mkdir -p "$stage" dist
cp "out/particles$exe" README.md LICENSE NOTICE PATCHES.md "$stage/"
if [ -n "$exe" ]; then
  (cd "$stage" && zip -qr "../../dist/particles-$target.zip" .)
else
  tar -czf "dist/particles-$target.tar.gz" -C "$stage" .
fi
ls dist
