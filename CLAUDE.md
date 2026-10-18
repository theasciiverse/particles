# particles (Asciiverse packaging)

flarn2006's interactive particle fountain, `particles.cpp` and `delayms.h`
from his MiscPrograms repository, C++ on curses, MIT (no copyright line
upstream: NOTICE credits him); catalog title "Particle Fountain", kind
`art`. Not our code: keep changes small, list every one in PATCHES.md.

- History: `git filter-repo` of MiscPrograms keeping only the two files
  and LICENSE (branch `upstream-files`). Remotes: `upstream` is the whole
  github.com/flarn2006/MiscPrograms, `origin` is
  github.com/theasciiverse/particles.
- Branch `asciiverse` = `upstream-files` plus our commits.
- Release: tag `v<version>-av.<n>` (now `v2017.02.19-av.1`) and push only
  that tag; the workflow runs on `*-av.*` tags.
- av starts it as `particles`.
- Build: `asciiverse/build.sh`. Static, in a copy of the tree: `docker run
  --rm --cpus 4 --memory 8g -v "$PWD":/src -w /src alpine:3.22 sh -c 'apk
  add build-base ncurses-dev ncurses-static && LIBS=-lncursesw
  LDFLAGS="-static -s" asciiverse/build.sh'`.
- Preview: `asciiverse/record-preview.py out/particles asciiverse/particles.cast`.
