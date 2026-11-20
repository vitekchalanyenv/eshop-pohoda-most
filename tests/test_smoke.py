"""Smoke test: ověřuje jen, že prostředí funguje a balíček jde importovat.

Když projde, máš správně nainstalovaný Python, uv i pytest.
"""

from pathlib import Path

import most

DATA = Path(__file__).parent.parent / "data" / "vstup"


def test_balicek_jde_importovat():
    assert most.__version__ == "0.1.0"


def test_vstupni_data_existuji():
    assert (DATA / "feed_produkty.xml").exists()
    assert (DATA / "sklad_export.csv").exists()
