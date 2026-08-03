import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from src.Issues_report.infrastructure.handle_issues_reports import IssuesHandler  # Update the path accordingly

# Test for successful data loading
@patch('pandas.read_csv')
def test_load_issues_data(mock_read_csv):
    # Mock the dataframe that pandas.read_csv will return
    mock_read_csv.return_value = pd.DataFrame({
        'plz': [12345, 67890],
        'description': ['Valid report 1', 'Valid report 2'],
        'station_id': [1, 2]
    })

    issue_handler = IssuesHandler({'plz': 12345, 'description': 'Test report', 'station_id': 1})
    issue_handler.load_issues_data()

    # Ensure the dataframe is loaded correctly
    assert issue_handler.issues_dframe is not None
    assert len(issue_handler.issues_dframe) == 2
    assert issue_handler.issues_dframe['plz'].iloc[0] == 12345

# Test for submitting a valid issue
@patch('pandas.read_csv')
@patch('pandas.DataFrame.to_csv')
def test_submit_issue_valid(mock_to_csv, mock_read_csv):
    # Mock the dataframe returned by read_csv
    mock_read_csv.return_value = pd.DataFrame({
        'plz': [12345],
        'description': ['Existing report'],
        'station_id': [1]
    })

    issue_handler = IssuesHandler({'plz': 67890, 'description': 'New report', 'station_id': 2})
    issue_handler.load_issues_data()

    # Submit the issue
    issue_handler.submit_issue()

    # Check that the issue was added correctly
    assert len(issue_handler.issues_dframe) == 2
    assert issue_handler.issues_dframe['plz'].iloc[1] == 67890
    assert issue_handler.issues_dframe['description'].iloc[1] == 'New report'

    # Verify the to_csv method was called to save the updated dataframe
    mock_to_csv.assert_called_once_with(issue_handler._path, index=False)

# Test for submitting an issue when the dataframe is empty
@patch('pandas.read_csv')
@patch('pandas.DataFrame.to_csv')
def test_submit_issue_empty_dataframe(mock_to_csv, mock_read_csv):
    # Mock an empty dataframe returned by read_csv
    mock_read_csv.return_value = pd.DataFrame(columns=['plz', 'description', 'station_id'])

    issue_handler = IssuesHandler({'plz': 12345, 'description': 'New report', 'station_id': 1})
    issue_handler.load_issues_data()

    # Submit the issue
    issue_handler.submit_issue()

    # Check that the issue was added correctly to the empty dataframe
    assert len(issue_handler.issues_dframe) == 1
    assert issue_handler.issues_dframe['plz'].iloc[0] == 12345
    assert issue_handler.issues_dframe['description'].iloc[0] == 'New report'

    # Verify the to_csv method was called to save the updated dataframe
    mock_to_csv.assert_called_once_with(issue_handler._path, index=False)

# Test for handling invalid issue instance data
@patch('pandas.read_csv')
def test_submit_issue_invalid_data(mock_read_csv):
    # Mock the dataframe returned by read_csv
    mock_read_csv.return_value = pd.DataFrame({
        'plz': [12345],
        'description': ['Existing report'],
        'station_id': [1]
    })

    # Simulating invalid issue instance with missing data
    issue_handler = IssuesHandler({'plz': '', 'description': '', 'station_id': 0})

    issue_handler.load_issues_data()

    # Check if the issue instance data is invalid (for example, empty or incorrect data)
    assert issue_handler.issue_instance['plz'] == ''
    assert issue_handler.issue_instance['description'] == ''
    assert issue_handler.issue_instance['station_id'] == 0

