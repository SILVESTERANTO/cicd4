def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Hello from Python CI Lab!")
    print("2 + 3 =", add(2, 3))

tests/test_app.py

Create a tests folder, then inside it test_app.py:

from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0