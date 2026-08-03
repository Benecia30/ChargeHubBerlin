import pytest
from src.Issues_report.Domain.entities.report import Issue  # Replace 'your_module' with the actual module name

# Test for validate_plz method
def test_validate_plz_valid():
    issue = Issue(12345, "This is a valid description.", 1)
    assert issue.validate_plz() is True

def test_validate_plz_invalid_length():
    issue = Issue(1234, "This is a valid description.", 1)
    with pytest.raises(ValueError, match="Invalid postal code. Postal code must be a 5-digit number."):
        issue.validate_plz()

def test_validate_plz_invalid_type():
    issue = Issue("ABCDE", "This is a valid description.", 1)
    with pytest.raises(ValueError, match="Invalid postal code. Postal code must be a 5-digit number."):
        issue.validate_plz()

# Test for validate_description method
def test_validate_description_valid():
    issue = Issue(12345, "This is a valid description.", 1)
    assert issue.validate_description() is True

def test_validate_description_invalid_length():
    issue = Issue(12345, "Short", 1)
    with pytest.raises(ValueError, match="Invalid report description. Description must be a string with at least 10 characters."):
        issue.validate_description()

def test_validate_description_invalid_type():
    issue = Issue(12345, 12345, 1)
    with pytest.raises(ValueError, match="Invalid report description. Description must be a string with at least 10 characters."):
        issue.validate_description()


def test_validate_station_id_invalid_type():
    issue = Issue(12345, "This is a valid description.", "One")
    with pytest.raises(ValueError, match="Invalid station ID. Station ID must be an integer."):
        issue.validate_station_id()