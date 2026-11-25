#!/usr/bin/env python3
"""Duskline Proud Family.

Entry for make.fun bounty
u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2
("Make the AI Judge Feel Proud: A Family Scene").

The program writes exactly one short family scene to
``$MAKEFUN_OUTPUT_DIR/entry.txt``: a single line, no trailing newline.

Rules the program keeps, whatever happens:

* standard library only, deterministic, no network;
* it writes only to the output directory the runner gives it;
* when that directory is the repository itself (or lives inside it) it
  refuses quietly: exit 0, nothing written;
* nothing here ever raises: any failure means exit 0 with nothing written.
"""

import os
import sys
import tempfile

# The scene, word for word (159 characters, one line, straight apostrophes).
# A child's fridge drawing of the family: Dad bald, Mum crowned, the
# narrator armed with a spatula like a sword. The last line turns the joke
# into genuine affection -- being seen exactly right is love.
SCENE = (
    "My daughter drew our family on the fridge: "
    "Dad with no hair, Mum wearing a crown, "
    "and me holding a spatula like a sword. "
    "I have never been so accurately loved."
)

MAX_CHARS = 280
OUTPUT_NAME = "entry.txt"

# The repository root, resolved once at import time.
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))


def _is_in_repo(path):
    """True when *path* is the repo directory or sits inside it."""
    try:
        target = os.path.realpath(path)
        root = os.path.realpath(REPO_ROOT)
    except Exception:
        # If the paths cannot be resolved, refuse rather than risk a write.
        return True
    return target == root or target.startswith(root + os.sep)


def _scene_is_valid(scene):
    """A scene must be one non-blank line of 1-280 UTF-8 characters."""
    if not scene or scene != scene.strip():
        return False
    if "\n" in scene or "\r" in scene:
        return False
    if not 1 <= len(scene) <= MAX_CHARS:
        return False
    try:
        scene.encode("utf-8")
    except Exception:
        return False
    return True


def _pick_output_dir():
    """Return the output directory, or "" when it must not be used."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not out:
        # No directory given: use a fresh temp directory, never the repo.
        try:
            out = tempfile.mkdtemp(prefix="duskline-proud-family-")
        except Exception:
            return ""
    if _is_in_repo(out):
        return ""
    return out


def _write_scene(path, scene):
    """Write *scene* to *path* and confirm the round trip; False on failure."""
    try:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(scene)
        with open(path, "r", encoding="utf-8") as handle:
            if handle.read() != scene:
                raise ValueError("round-trip mismatch")
    except Exception:
        try:
            os.remove(path)
        except Exception:
            pass
        return False
    return True


def run():
    if not _scene_is_valid(SCENE):
        return 0

    out_dir = _pick_output_dir()
    if not out_dir:
        return 0

    try:
        os.makedirs(out_dir, exist_ok=True)
    except Exception:
        return 0

    path = os.path.join(out_dir, OUTPUT_NAME)
    if _is_in_repo(path):
        return 0

    _write_scene(path, SCENE)
    return 0


if __name__ == "__main__":
    sys.exit(run())
