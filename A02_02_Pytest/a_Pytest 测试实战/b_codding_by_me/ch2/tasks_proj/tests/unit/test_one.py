import pytest


def test_work():
    assert (1,2,3) == (1,2,3)

@pytest.mark.run_this_task
def test_love():
    assert(1,2,3) == (1,3,4)










