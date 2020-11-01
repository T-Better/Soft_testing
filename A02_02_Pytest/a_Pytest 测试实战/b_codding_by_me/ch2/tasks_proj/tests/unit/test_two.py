import pytest


def test_home():
    assert 2 == 3


@pytest.mark.run_this_task
def test_bike():
    assert 3 == 3


def test_drive():
    assert 2 == 1

def test_book():
    print("张三是个猪")
    assert 1!=1
