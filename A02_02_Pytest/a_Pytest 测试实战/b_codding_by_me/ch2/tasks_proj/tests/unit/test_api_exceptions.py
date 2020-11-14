import pytest
import tasks

def test_add_raises():
    """add() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.add(task="not a Task object")
