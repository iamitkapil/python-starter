# tests/test_vuln_sql.py
import sqlite3
import pytest
from app.vuln_sql import find_users_vulnerable, find_users_secure, init_db

def test_vulnerable_returns_expected():
    # simple safe query behavior
    res = find_users_vulnerable("ali")
    assert any("alice" in row for row in [r[1] for r in res])

def test_secure_behaves_same():
    res_v = find_users_vulnerable("bob")
    res_s = find_users_secure("bob")
    assert [r[1] for r in res_v] == [r[1] for r in res_s]

def test_vulnerable_allows_injection():
    # This demonstrates that constructing a payload can alter SQL logic.
    # We craft a payload that closes the LIKE pattern and appends OR 1=1 to return all rows.
    payload = "%' OR 1=1 --"
    res = find_users_vulnerable(payload)
    assert len(res) >= 3  # injection returns multiple rows (demonstrates vulnerability)

    # The secure version should NOT be tricked by the same payload
    res_secure = find_users_secure(payload)
    # Secure uses parameterized LIKE, which will treat payload as literal pattern; likely returns 0
    assert len(res_secure) < len(res)
