"""Test the Task data type"""
from tasks import Task  # 为啥tasks中没有Task呢？

def test_asdict():
    """_asdict() should return a dictionary"""
    t_task = Task('do something','okken',True,21)  # TODO 1 ?什么意思？
    t_dict = t_task.asdict()  # TODO 2 ?什么意思？
    expected = {'summary':'do something',
                'owner':'okken',
                'done':True,'id':21}
    assert t_dict == expected

def test_replace():
    """replace() shoule change passed in fields"""
    t_before = Task('finish book','brian',False)  # TODO 3 ?什么意思？
    t_after = t_before._replace(id=10,done=True)  # TODO 4 ?什么意思？
    t_expected = Task('finish book','brian',True,10)
    assert t_after == t_expected

def test_defaults():
    """Using no parameters should invoke defaults"""
    t1 = Task()
    t2 = Task(None,None,False, None)
    assert t1 == t2

def test_member_access():
    """Check field functionality of namedtuple"""
    t = Task('buy milk','brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done,t.id) == (False,None)
