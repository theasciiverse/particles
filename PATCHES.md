# Changes from upstream

This is the Asciiverse packaging of flarn2006's interactive particle
fountain, `particles.cpp` (with its `delayms.h`) from
[github.com/flarn2006/MiscPrograms](https://github.com/flarn2006/MiscPrograms),
C++ on curses. The repository was made with `git filter-repo`, keeping only
`particles.cpp`, `delayms.h` and `LICENSE` with their upstream commits
(branch `upstream-files`, last upstream change `e6c9e57`, 2017-02-19, the
switch to the MIT licence; upstream's own hash for it is `70774d3`). The
`upstream` remote is the whole MiscPrograms repository; the `asciiverse`
branch carries the changes below. Upstream has no tags or versions, so the
version here is the date of the last upstream change, 2017.02.19.

## Licence

MIT. Upstream's LICENSE has the MIT terms but no copyright line; NOTICE
credits flarn2006 by name, as the repository and every commit do. The
commit "Change to MIT license" (2017) is the author's own relicensing of
the whole repository.

## Code

- **Q and Esc quit as well as q.** The help line says `<Q>`, but only a
  lowercase q quit. The help now says `<Q/Esc>`. Other keys keep their
  jobs, so not every key quits. Ctrl+C was already clean: curses puts the
  terminal back (exit status 1).
- **The emitter stays on the screen after a resize.** On `KEY_RESIZE` the
  size is read again and an emitter that would now be off the screen goes
  back to its starting place (a quarter across, half down). Upstream read
  the size once. Under PDCurses `resize_term(0, 0)` comes first.

## Packaging

- `README.md` and `NOTICE` are ours (upstream's README is about another
  program in the collection).
- `asciiverse/build.sh` and `asciiverse/package.sh` build and pack one
  target; the compiler and curses library come from the environment.
- `.github/workflows/release.yml`: av archives for Linux (static musl,
  x86-64 and ARM64), macOS (x86-64 and ARM64, system ncurses) and Windows
  (x86-64, MinGW and wide PDCurses 3.9), plus SHA256SUMS. Runs on our tags
  only (`*-av.*`).
- `asciiverse/record-preview.py` records `asciiverse/particles.cast`, the
  catalog preview: the fountain at 100x30 with its help, then gravity,
  speed, a longer life, wind and the emitter moved, then q.

av starts it as `particles` with no arguments.

## Checked

- Linux, native (glibc, ncurses) and static (Alpine 3.22) builds, in tmux
  at 100x30: q, Q and Esc quit with status 0, Ctrl+C with status 1, the
  terminal settings put back each time; the emitter moved right and the
  window resized to 40x12 and 120x40 keeps the emitter on the screen.
- Windows: cross-built with MinGW against PDCurses 3.9 (wincon, wide) and
  run under Wine: particles drawn, q quits with status 0. Resizing there is
  unchecked.
- macOS: not built here.
