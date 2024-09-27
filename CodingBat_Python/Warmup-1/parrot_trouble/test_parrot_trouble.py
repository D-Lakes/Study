import parrot_trouble as p

def test_parrot_trouble():
    assert p.parrot_trouble(True, 6) == True
    assert p.parrot_trouble(True, 7) == False
    assert p.parrot_trouble(False, 6) == False

