import sleep_in as s

def test_sleep_in():
    assert s.sleep_in(False, False) == True
    assert s.sleep_in(True, False) == False
    assert s.sleep_in(False, True) == True
    

