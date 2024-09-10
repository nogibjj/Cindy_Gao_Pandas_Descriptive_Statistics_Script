from main import add, subtract


def test_add():
    """testing out add function"""
    assert add(2, 2) == 4
    assert add(1, 3) == 4


def test_subtract():
    assert subtract(9, 3) == 6
    assert subtract(27, 10) == 17


if __name__ == "__main__":
    test_add()
