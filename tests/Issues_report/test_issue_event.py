import pytest
from src.Issues_report.Domain.entities.report import Issue
from src.Issues_report.Domain.events.create_report_event import CreateReportEvent  # Update the path accordingly


# Test for valid issue generation
def test_generate_issue_event_valid():
    event = CreateReportEvent(12345, "This is a valid description.", 1)
    event.generate_issue_event()

    assert event.issue_instance == {
        'plz': 12345,
        'description': "This is a valid description.",
        'station_id': 1,
    }


# Test for invalid postal code
def test_generate_issue_event_invalid_plz():
    event = CreateReportEvent(1234, "This is a valid description.", 1)
    with pytest.raises(ValueError, match="Invalid postal code. Postal code must be a 5-digit number."):
        event.generate_issue_event()


# Test for invalid station ID
def test_generate_issue_event_invalid_station_id():
    event = CreateReportEvent(12345, "This is a valid description.", "One")
    with pytest.raises(ValueError, match="Invalid station ID. Station ID must be an integer."):
        event.generate_issue_event()


# Test for invalid description (too short)
def test_generate_issue_event_invalid_description_length():
    event = CreateReportEvent(12345, "Short", 1)
    with pytest.raises(ValueError,
                       match="Invalid report description. Description must be a string with at least 10 characters."):
        event.generate_issue_event()


# Test for invalid description type (not a string)
def test_generate_issue_event_invalid_description_type():
    event = CreateReportEvent(12345, 12345, 1)
    with pytest.raises(ValueError,
                       match="Invalid report description. Description must be a string with at least 10 characters."):
        event.generate_issue_event()


# Test for issue instance not generated when validation fails
def test_issue_instance_not_generated_on_failure():
    event = CreateReportEvent(12345, "Short", 1)
    with pytest.raises(ValueError):
        event.generate_issue_event()
    assert event.issue_instance == {}
