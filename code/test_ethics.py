#!/usr/bin/env python3
"""Tests pour ethics.py"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ethics import DecisionLog


def test_add_decision():
    log = DecisionLog()
    d = log.add_decision("Aether", "Test decision", "Parce que test", "propose")
    assert d.who == "Aether"
    assert len(log.decisions) == 1
    print("OK  test_add_decision")


def test_add_alert():
    log = DecisionLog()
    a = log.add_alert("Lumen", "Risque de confusion Message / physique", "THEORIE")
    assert a.who == "Lumen"
    assert len(log.alerts) == 1
    print("OK  test_add_alert")


def test_summary_contains():
    log = DecisionLog()
    log.add_decision("Bego", "Valider structure repos", "Organisation", "fait")
    text = log.summary()
    assert "Valider structure repos" in text
    assert "Bego" in text
    print("OK  test_summary_contains")


if __name__ == "__main__":
    test_add_decision()
    test_add_alert()
    test_summary_contains()
    print("TOUS LES TESTS ethics SONT PASSES")
