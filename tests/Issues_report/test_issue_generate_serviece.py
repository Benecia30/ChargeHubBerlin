import pytest
from unittest.mock import patch, MagicMock
from src.Issues_report.Domain.entities.report import Issue
from src.Issues_report.infrastructure.handle_issues_reports import IssuesHandler
from src.Issues_report.Domain.events.create_report_event import CreateReportEvent
from src.Issues_report.Application.stations_issues_report_service import IssuesReportService  # Update the path accordingly

# Test for successful report submission
@patch.object(IssuesHandler, 'load_issues_data')
@patch.object(IssuesHandler, 'submit_issue')
@patch.object(CreateReportEvent, 'generate_issue_event')
def test_submit_report_valid(mock_generate_issue_event, mock_submit_issue, mock_load_issues_data):
    # Create a mock of the Issue instance
    mock_generate_issue_event.return_value = None
    mock_load_issues_data.return_value = None
    mock_submit_issue.return_value = None

    # Create an instance of the IssuesReportService
    service = IssuesReportService(plz=12345, report_description="Valid report description", station_id=1)

    # Call the submit_report method
    service.submit_report()

    # Check if the generate_issue_event method was called
    mock_generate_issue_event.assert_called_once()

    # Check if the load_issues_data method was called
    mock_load_issues_data.assert_called_once()

    # Check if the submit_issue method was called
    mock_submit_issue.assert_called_once()


# Test for checking correct interaction with the IssuesHandler
@patch.object(IssuesHandler, 'load_issues_data')
@patch.object(IssuesHandler, 'submit_issue')
@patch.object(CreateReportEvent, 'generate_issue_event')
def test_submit_report_interaction_with_handler(mock_generate_issue_event, mock_submit_issue, mock_load_issues_data):
    # Create a mock of the Issue instance
    mock_generate_issue_event.return_value = None
    mock_load_issues_data.return_value = None
    mock_submit_issue.return_value = None

    # Create an instance of the IssuesReportService with valid data
    service = IssuesReportService(plz=12345, report_description="Report with valid description", station_id=1)

    # Call the submit_report method
    service.submit_report()

    # Check if IssuesHandler's load_issues_data method was called once
    mock_load_issues_data.assert_called_once()

    # Check if IssuesHandler's submit_issue method was called once
    mock_submit_issue.assert_called_once()
