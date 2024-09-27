from pos_neg import pos_neg

def test_pos_neg():
    assert pos_neg(1,-1,False) == True
    assert pos_neg(-1,1,False) == True
    assert pos_neg(-4,-5,True) == True
