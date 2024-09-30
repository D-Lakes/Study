import front3 as f

def test_front3():
    assert f.front3('Java') == 'JavJavJav'
    assert f.front3('Chocolate') == 'ChoChoCho'
    assert f.front3('abc') == 'abcabcabc'

