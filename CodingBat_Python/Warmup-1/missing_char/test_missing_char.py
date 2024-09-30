import missing_char as m

def test_missing_char():
    assert m.missing_char("kitten", 1) == "ktten"
    assert m.missing_char("kitten", 0) == "itten"
    assert m.missing_char("kitten", 4) == "kittn"
