#!/usr/bin/env python3
"""Records asciiverse/particles.cast, the catalog preview, at 100x30: the
fountain as av starts it, then a few keys played the way a person would
(gravity, more speed, a longer life, wind, the emitter moved), then q.
Needs asciinema 3.
Usage: record-preview.py <particles binary> <out.cast>"""
import fcntl, os, pty, select, shutil, struct, sys, tempfile, termios, time

binary, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
home = tempfile.mkdtemp()
shutil.copy(binary, os.path.join(home, "particles"))
env = dict(os.environ, HOME=home, PATH=home + ":" + os.environ["PATH"],
           TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8")
pid, fd = pty.fork()
if pid == 0:
    os.chdir(home)  # nothing in the recording names a local path
    fcntl.ioctl(0, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q",
        "--window-size", "100x30", "--title", "particles",
        "--capture-env", "TERM,COLORTERM,LANG", "-c", "particles", out], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))

def pump(t):
    end = time.time() + t
    while time.time() < end:
        if select.select([fd], [], [], 0.05)[0]:
            try:
                os.read(fd, 1 << 16)
            except OSError:
                return

def keys(seq, gap=0.12):
    for k in seq:
        os.write(fd, k)
        pump(gap)

UP, DOWN, LEFT, RIGHT = b"\x1b[A", b"\x1b[B", b"\x1b[D", b"\x1b[C"
pump(4.0)                          # the fountain with its help
keys([b"`", b"`"]); pump(2.0)      # help off, the emitter stays
keys([b"s"] * 4); pump(3.0)        # gravity
keys([b"+"] * 8); pump(3.0)        # faster
keys([b"]"] * 4); pump(3.0)        # a longer life
keys([b"a"] * 3); pump(2.5)        # wind from the right
keys([RIGHT] * 12, 0.08); pump(2.0)
keys([b"d"] * 6); pump(2.5)        # wind from the left
keys([UP] * 6, 0.08); pump(2.5)
os.write(fd, b"q")
for _ in range(50):
    if os.waitpid(pid, os.WNOHANG)[0]:
        break
    time.sleep(0.1)
else:
    os.kill(pid, 15)
shutil.rmtree(home, ignore_errors=True)
