from makes10 import makes10


def test_makes10():
   assert makes10(9, 10) == True
   assert makes10(9, 9) == False
   assert makes10(1, 9) == True
