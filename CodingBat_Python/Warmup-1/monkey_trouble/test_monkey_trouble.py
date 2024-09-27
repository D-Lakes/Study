import monkey_trouble as m

def test_monkey_trouble():
    assert m.monkey_trouble(True,True) == True
    assert m.monkey_trouble(False,False) == True
    assert m.monkey_trouble(True,False) == False
