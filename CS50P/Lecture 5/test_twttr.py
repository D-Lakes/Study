from twttr import shorten

def test_shorten():
    assert shorten('word') == 'wrd'
