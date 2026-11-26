#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign line to /output/entry.txt (or ./output/entry.txt
when /output is not writable, e.g. local runs). The line is fixed so
every run is byte-identical.
"""

import os
import sys

SIGN = "WARNING: Haunted server room. The ghost has root and reboots anyone who ignores his tickets at 3 AM."


def main() -> int:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        probe = os.path.join(out_dir, ".probe")
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("ok")
        os.remove(probe)
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(SIGN + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
