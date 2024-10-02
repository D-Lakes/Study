import string_bits as s

def test_string_bits():
    assert s.string_bits("Hello") == "Hlo"
    assert s.string_bits("Hi") == "H"
    assert s.string_bits("Heeololeo") == "Hello"
