import front_back as f

def test_front_back():
    assert f.front_back('code')== 'eodc' 
    assert f.front_back('a') == 'a' 
    assert f.front_back('ab') == 'ba' 
    
