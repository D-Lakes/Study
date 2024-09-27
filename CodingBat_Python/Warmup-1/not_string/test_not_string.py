from not_string import not_string

def test_not_string():
    assert not_string('candy') == 'not candy'
    assert not_string('x') == 'not x'
    assert not_string('not bad') == 'not bad'
