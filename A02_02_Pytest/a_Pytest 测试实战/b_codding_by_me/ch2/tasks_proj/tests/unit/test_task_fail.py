from tasks import Task

def test_task_equality():
    """Different tasks should not be equal"""
    t1 = Task("sit there","brian")
    t2 = Task("do something","okken")
    assert t1 == t2

def test_dict_equality():
    """Different tasks compared as dicts should not be equal"""
    t1_dict = Task("make sandwich","okken")._asdict()
    t2_dict = Task("make sandwich","okkem")._asdict()  # ._asdict()什么意思？
    assert t1_dict == t2_dict