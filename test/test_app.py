from test.app import add, subtract

def test_add():

    assert add(2,3)==5

def test_subtract():

    assert subtract(3,2)==1

def test_subtract_neg():

    assert subtract(2,3)==-1

def test_add_neg():

    assert add(-2,3)==1

def test_add_neg2():

    assert add(2,-3)==-1

def test_subtract_neg2():

    assert subtract(-2,3)==-5

