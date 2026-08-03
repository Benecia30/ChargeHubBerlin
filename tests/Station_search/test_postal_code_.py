import pytest
from src.Station_search.Domain.entities.entities import Postalcode  # Replace 'your_module_name' with the actual module name

def test_valid_postalcode():
    postalcode = Postalcode(10116)
    assert postalcode.check_dtype() is True
    assert postalcode.check_length() is True
    assert postalcode.check_range() is True

def test_invalid_dtype():
    with pytest.raises(TypeError, match="plz must be of type <class 'int'>"):
        postalcode = Postalcode("10116")
        postalcode.check_dtype()

def test_invalid_length():
    with pytest.raises(ValueError, match="Invalid postal code: {}. Postal code must have 5 digits.".format(str(123))):
        postalcode = Postalcode(123)
        postalcode.check_length()

    with pytest.raises(ValueError, match="Invalid postal code: {}. Postal code must have 5 digits.".format(str(123456))):
        postalcode = Postalcode(123456)
        postalcode.check_length()

def test_out_of_range_postalcode():
    with pytest.raises(ValueError, match="PLZ must be between 10115 and 14200"):
        postalcode = Postalcode(10000)
        postalcode.check_range()

    with pytest.raises(ValueError, match="PLZ must be between 10115 and 14200"):
        postalcode = Postalcode(15000)
        postalcode.check_range()

def test_edge_cases():
    # Test minimum boundary
    postalcode = Postalcode(10115)
    assert postalcode.check_dtype() is True
    assert postalcode.check_length() is True
    assert postalcode.check_range() is True

    # Test maximum boundary
    postalcode = Postalcode(14200)
    assert postalcode.check_dtype() is True
    assert postalcode.check_length() is True
    assert postalcode.check_range() is True
