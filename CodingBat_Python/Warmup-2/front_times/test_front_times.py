import front_times as f

def test_front_times():
    assert f.front_times('Chocolate', 2) == "ChoCho"
    assert f.front_times('Chocolate', 3) == "ChoChoCho"
    assert f.front_times('Abc', 3) == "AbcAbcAbc"
