"""Seed test, so a shard repo's CI has something to run."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app import add
from shard_app.settings import MAX_SETTINGS_BYTES, is_rejected


def test_add() -> None:
    assert add(2, 3) == 5


def test_oversized_settings_file_is_rejected() -> None:
    settings = Path(__file__).resolve().parents[1] / ".vera" / "settings.yaml"
    assert settings.stat().st_size > MAX_SETTINGS_BYTES
    assert is_rejected(settings)
