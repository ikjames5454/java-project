from add import add_number


def test_addition():
    assert add_number(5, 6) == 11
    assert add_number(5, 10) == 15
    assert add_number(5, 13) == 18
