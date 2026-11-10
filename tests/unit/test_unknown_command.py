"""Unit tests for unknown-command handling in mlp_cli.main."""
import sys

import pytest

import mlp_cli


@pytest.mark.unit
def test_unknown_command_exits_nonzero(monkeypatch, capsys, tmp_path):
    """An unknown command must fail instead of exiting 0."""
    monkeypatch.setattr(
        sys,
        "argv",
        ["mlp_cli.py", "bogus", str(tmp_path / "out"), str(tmp_path / "data")],
    )
    with pytest.raises(SystemExit) as exc_info:
        mlp_cli.main()
    assert exc_info.value.code == 2
    captured = capsys.readouterr()
    assert "Unknown command" in captured.err
