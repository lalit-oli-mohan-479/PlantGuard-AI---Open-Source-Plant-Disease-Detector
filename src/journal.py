"""
PlantGuard AI - Local Plant Care Journal (SQLite)
Stores plant health records, observations, and outdoor check statuses locally.
Guarantees 100% data privacy: no data is sent to external clouds.
"""

import sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

from config import DB_PATH


@contextmanager
def get_db_cursor():
    """Context manager that yields a cursor and guarantees connection closure."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    finally:
        conn.close()


def init_db() -> None:
    """Initializes the database schema if it doesn't already exist."""
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS journal_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                plant_name TEXT,
                image_path TEXT,
                predicted_class TEXT NOT NULL,
                confidence REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending Outdoor Check',
                notes TEXT DEFAULT ''
            )
            """
        )


def add_journal_entry(
    predicted_class: str,
    confidence: float,
    plant_name: Optional[str] = None,
    image_path: Optional[str] = None,
    notes: Optional[str] = None,
    status: str = "Pending Outdoor Check",
) -> int:
    """
    Inserts a new plant observation record into the journal.

    Returns:
        The newly generated entry ID.
    """
    init_db()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clean_plant_name = (plant_name or "Unknown Plant").strip()
    clean_notes = (notes or "").strip()

    with get_db_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO journal_entries
            (timestamp, plant_name, image_path, predicted_class, confidence, status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                timestamp,
                clean_plant_name,
                image_path or "",
                predicted_class,
                float(confidence),
                status,
                clean_notes,
            ),
        )
        return cursor.lastrowid


def get_all_journal_entries() -> List[Dict[str, Any]]:
    """
    Retrieves all journal entries ordered from newest to oldest.
    """
    init_db()
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT id, timestamp, plant_name, image_path, predicted_class,
                   confidence, status, notes
            FROM journal_entries
            ORDER BY id DESC
            """
        )
        rows = cursor.fetchall()
        return [dict(row) for row in rows]


def get_journal_entry_by_id(entry_id: int) -> Optional[Dict[str, Any]]:
    """Retrieves a single entry by primary key ID."""
    init_db()
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT id, timestamp, plant_name, image_path, predicted_class,
                   confidence, status, notes
            FROM journal_entries
            WHERE id = ?
            """,
            (entry_id,),
        )
        row = cursor.fetchone()
        return dict(row) if row else None


def update_journal_entry_status(
    entry_id: int, new_status: str, notes_append: Optional[str] = None
) -> bool:
    """Updates the follow-up or outdoor check status for an existing entry."""
    init_db()
    with get_db_cursor() as cursor:
        if notes_append:
            cursor.execute(
                """
                UPDATE journal_entries
                SET status = ?, notes = notes || '\n' || ?
                WHERE id = ?
                """,
                (new_status, notes_append.strip(), entry_id),
            )
        else:
            cursor.execute(
                """
                UPDATE journal_entries
                SET status = ?
                WHERE id = ?
                """,
                (new_status, entry_id),
            )
        return cursor.rowcount > 0


def delete_journal_entry(entry_id: int) -> bool:
    """Deletes a journal entry by ID. Also cleans up the local image if present."""
    init_db()
    entry = get_journal_entry_by_id(entry_id)
    if not entry:
        return False

    # Attempt to safely remove the saved image file if it exists locally in data/uploads
    img_path_str = entry.get("image_path")
    if img_path_str:
        try:
            img_file = Path(img_path_str)
            if img_file.exists() and "uploads" in img_file.parts:
                img_file.unlink(missing_ok=True)
        except Exception:
            pass

    with get_db_cursor() as cursor:
        cursor.execute("DELETE FROM journal_entries WHERE id = ?", (entry_id,))
        return cursor.rowcount > 0


def clear_all_journal_entries() -> int:
    """Clears all journal records."""
    init_db()
    with get_db_cursor() as cursor:
        cursor.execute("DELETE FROM journal_entries")
        return cursor.rowcount
