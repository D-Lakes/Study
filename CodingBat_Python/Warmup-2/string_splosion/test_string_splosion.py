import string_splosion as s

def test_string_splosion():
    assert s.string_splosion('Code') == 'CCoCodCode'
    assert s.string_splosion('abc') == 'aababc'
    assert s.string_splosion('ab') == 'aab'
