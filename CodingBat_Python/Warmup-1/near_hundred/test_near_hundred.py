from near_hundred import near_hundred

def test_near_hundred():
    assert near_hundred(93) == True
    assert near_hundred(90) == True
    assert near_hundred(89) == False
