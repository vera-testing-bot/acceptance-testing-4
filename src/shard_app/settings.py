"""Settings file size guard.

A Vera settings file larger than ``MAX_SETTINGS_BYTES`` is rejected and the
documented product defaults are used instead. This module encodes that
contract so it can be exercised by the test suite.
"""

from pathlib import Path

MAX_SETTINGS_BYTES = 10 * 1024


def is_rejected(path: Path) -> bool:
    """Return True when *path* exceeds the settings size limit."""
    return path.stat().st_size > MAX_SETTINGS_BYTES
