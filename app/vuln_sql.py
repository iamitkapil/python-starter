# vuln_sql.py
import sqlite3
from typing import List, Tuple

DB_PATH = ":memory:"


def init_db(conn: sqlite3.Connection):
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.executemany(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        [("alice", "alicepwd"), ("bob", "bobpwd"), ("mallory", "mallorypwd")]
    )
    conn.commit()


# VULNERABLE: uses f-string to build SQL -> SQL Injection possible
def find_users_vulnerable(search: str) -> List[Tuple[int, str, str]]:
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    # Dangerous: directly interpolating user input into SQL
    query = f"SELECT id, username, password FROM users WHERE username LIKE '%{search}%'"
    cursor = conn.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# SECURE version (for reference)
def find_users_secure(search: str) -> List[Tuple[int, str, str]]:
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    # Parameterized query prevents SQL injection
    cursor = conn.execute("SELECT id, username, password FROM users WHERE username LIKE ?", (f"%{search}%",))
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == "__main__":
    print("Vulnerable search for 'ali':", find_users_vulnerable("ali"))
    print("Secure  search for 'ali':", find_users_secure("ali"))
