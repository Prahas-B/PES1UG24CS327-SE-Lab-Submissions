"""Programme schedule for a radio station.

Books show slots, lists the morning shows, checks timing between
slots and removes slots, using an in-memory SQLite database.
"""

import os
import sqlite3

# Read the studio password from the environment instead of hardcoding it.
STUDIO_PASSWORD = os.environ.get("STUDIO_PASSWORD")
NOON = 12


def create_schedule():
    """Create and return a connection holding an empty slots table."""
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE slots (id INTEGER PRIMARY KEY, show TEXT, host TEXT, "
        "start_hour INTEGER, minutes INTEGER)"
    )
    return conn


def add_slot(conn, show, host, start_hour, minutes):
    """Book a show slot and return its id."""
    cursor = conn.execute(
        "INSERT INTO slots (show, host, start_hour, minutes) "
        "VALUES (?, ?, ?, ?)",
        (show, host, start_hour, minutes),
    )
    return cursor.lastrowid


def booked_minutes(conn):
    """Return the total number of minutes currently booked."""
    total = conn.execute("SELECT SUM(minutes) FROM slots").fetchone()[0]
    return total or 0


def slot_label(show, host):
    """Return a human-readable label for a slot."""
    return f"{show} hosted by {host}"


def overlap_free(start_hour, minutes, next_start_hour):
    """Return True if a slot ends before the next one starts."""
    return start_hour * 60 + minutes <= next_start_hour * 60


def morning_shows(conn):
    """Return the names of all shows that start before noon."""
    if booked_minutes(conn) > 0:
        rows = conn.execute(
            "SELECT show FROM slots WHERE start_hour < ?", (NOON,)
        )
        return [row[0] for row in rows]
    return []


def remove_slot(conn, slot_id):
    """Remove the slot with the given id."""
    conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Run a short demonstration of the schedule."""
    conn = create_schedule()
    add_slot(conn, "Sunrise Beats", "Vik", 7, 60)
    midday_id = add_slot(conn, "Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free(7, 60, 13), morning_shows(conn))
    remove_slot(conn, midday_id)
    conn.close()


if __name__ == "__main__":
    main()
