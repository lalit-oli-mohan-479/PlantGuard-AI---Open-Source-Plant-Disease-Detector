"""
Unit tests for PlantGuard AI Plant Care Journal (SQLite).
"""

import tempfile
from pathlib import Path
import pytest

from src import journal


@pytest.fixture(autouse=True)
def temporary_db(monkeypatch):
    """Use a temporary database path for each test to keep tests isolated."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        temp_db_path = Path(tmp.name)

    monkeypatch.setattr(journal, "DB_PATH", temp_db_path)
    journal.init_db()

    yield temp_db_path

    try:
        temp_db_path.unlink(missing_ok=True)
    except Exception:
        pass


def test_add_and_retrieve_entry():
    """Test inserting a journal entry and retrieving all entries."""
    entry_id = journal.add_journal_entry(
        plant_name="Roma Tomato",
        predicted_class="Tomato with Early Blight",
        confidence=0.942,
        notes="Noticed brown spots on lower leaves.",
        status="Pending Outdoor Check",
    )
    assert entry_id > 0

    entries = journal.get_all_journal_entries()
    assert len(entries) == 1
    first = entries[0]
    assert first["id"] == entry_id
    assert first["plant_name"] == "Roma Tomato"
    assert first["predicted_class"] == "Tomato with Early Blight"
    assert round(first["confidence"], 2) == 0.94
    assert first["status"] == "Pending Outdoor Check"
    assert "brown spots" in first["notes"]


def test_get_entry_by_id():
    """Test retrieving specific entry by its ID."""
    entry_id = journal.add_journal_entry(
        plant_name="Bell Pepper",
        predicted_class="Healthy Bell Pepper Plant",
        confidence=0.98,
    )
    entry = journal.get_journal_entry_by_id(entry_id)
    assert entry is not None
    assert entry["plant_name"] == "Bell Pepper"

    non_existent = journal.get_journal_entry_by_id(99999)
    assert non_existent is None


def test_update_entry_status():
    """Test marking outdoor inspection complete in journal entry."""
    entry_id = journal.add_journal_entry(
        plant_name="Yukon Gold Potato",
        predicted_class="Potato with Late Blight",
        confidence=0.88,
        status="Pending Outdoor Check",
    )

    success = journal.update_journal_entry_status(
        entry_id=entry_id,
        new_status="Grass Touched: Inspected Outdoors",
        notes_append="Checked soil moisture and bagged two infected leaves.",
    )
    assert success is True

    updated = journal.get_journal_entry_by_id(entry_id)
    assert updated["status"] == "Grass Touched: Inspected Outdoors"
    assert "bagged two infected leaves" in updated["notes"]


def test_delete_entry():
    """Test deleting single entry by ID."""
    id1 = journal.add_journal_entry("Apple", 0.9, plant_name="Gala")
    id2 = journal.add_journal_entry("Grape", 0.85, plant_name="Concord")

    assert len(journal.get_all_journal_entries()) == 2
    deleted = journal.delete_journal_entry(id1)
    assert deleted is True

    remaining = journal.get_all_journal_entries()
    assert len(remaining) == 1
    assert remaining[0]["id"] == id2


def test_clear_all_entries():
    """Test clearing all records."""
    journal.add_journal_entry("Tomato", 0.9)
    journal.add_journal_entry("Pepper", 0.8)
    assert len(journal.get_all_journal_entries()) == 2

    cleared_count = journal.clear_all_journal_entries()
    assert cleared_count == 2
    assert len(journal.get_all_journal_entries()) == 0
