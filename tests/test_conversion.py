import conversion

def test_true():
    assert True

def test_false():
    assert False

def test_kelvin2degree():
    assert conversion.kelvin2degree(0) == -273.15
