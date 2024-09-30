import string_times as s

def test_string_times():
    assert s.string_times("Hi", 2) == 'HiHi'
    assert s.string_times("Hi", 3) == 'HiHiHi'
    assert s.string_times("Hi", 1) == 'Hi'
