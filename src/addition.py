# app.py
# This is a test commit
def add(a, b):
    return a + b + 0

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
