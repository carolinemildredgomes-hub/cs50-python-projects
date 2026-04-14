from um import count


def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1


def test_multiple_um():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3


def test_not_substring():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("summary") == 0
