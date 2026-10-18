# Particle Fountain

An interactive particle fountain in the terminal, in C++ on curses, by
flarn2006 (2013 to 2017), from his
[MiscPrograms](https://github.com/flarn2006/MiscPrograms) repository
(`particles.cpp` and `delayms.h`). An emitter sprays particles that age
from green through yellow to red and vanish; the keys change their speed,
life, gravity and wind, and move the emitter.

This repository holds only those two files and the licence, with their
upstream history, packaged for the Asciiverse catalog. Changes from
upstream are listed in PATCHES.md.

## Keys

- Arrows: move the emitter
- `-` and `+`: maximum velocity
- `a` and `d`: acceleration left and right (wind)
- `w` and `s`: acceleration up and down (gravity)
- `[` and `]`: maximum age
- `x`: clear all particles
- `` ` ``: change the display (help, emitter, both, neither)
- `q`, `Q` or Esc: quit

## Building

    c++ -O2 particles.cpp -lncurses -o particles

or `asciiverse/build.sh` (see the comments there for static, macOS and
Windows builds).

## Licence

MIT, see LICENSE and NOTICE.
