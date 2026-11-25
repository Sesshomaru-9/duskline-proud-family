#!/usr/bin/env python3
"""Duskline Proud Family — make.fun bounty u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.

One warm, funny family scene, written to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, standard library only, no network access. The program never
writes into its own repository: when the output directory is the repo itself
(or inside it) it refuses quietly and exits 0. Nothing here ever raises: any
failure exits 0 having written nothing.
"""

import os
import sys
import tempfile

LINE = (
    "My daughter drew our family on the fridge: Dad with no hair, Mum "
    "wearing a crown, and me holding a spatula like a sword. I have never "
    "been so accurately loved."
)
# The scene: a child's fridge drawing of the family — Dad bald, Mum crowned,
# the narrator armed with a spatula. Small, specific, wry, and the last line
# turns the joke into genuine affection: being seen exactly right is love.

HERE = os.path.dirname(os.path.abspath(__file__))


def _inside_repo(directory):
    """True when directory is the repo dir or lives inside it."""
    try:
        target = os.path.realpath(directory)
        root = os.path.realpath(HERE)
    except Exception:
        return True
    return target == root or target.startswith(root + os.sep)


def _valid(line):
    if not line or line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if not 1 <= len(line) <= 280:
        return False
    try:
        line.encode("utf-8")
    except Exception:
        return False
    return True


def run():
    if not _valid(LINE):
        return 0

    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not out:
        try:
            out = tempfile.mkdtemp(prefix="duskline-proud-family-")
        except Exception:
            return 0
    if _inside_repo(out):
        return 0

    try:
        os.makedirs(out, exist_ok=True)
    except Exception:
        return 0
    path = os.path.join(out, "entry.txt")
    if _inside_repo(path):
        return 0

    try:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(LINE)
        with open(path, "r", encoding="utf-8") as handle:
            if handle.read() != LINE:
                raise ValueError("round-trip mismatch")
    except Exception:
        try:
            os.remove(path)
        except Exception:
            pass
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(run())
