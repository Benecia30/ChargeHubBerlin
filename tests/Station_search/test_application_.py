import pytest
import pandas as pd
from unittest.mock import MagicMock

from src.Station_search.infrastructure.charging_station_repository import ChargingRepository
from src.Station_search.Application.search_stations_services import SearchService  # Replace with your actual path


@pytest.fixture
def mock_station_repository():
    # Mock the ChargingRepository class and its methods
    mock_repo = MagicMock(spec=ChargingRepository)

    # Simulate loading the charging data (no actual loading, just mock)
    mock_repo.load_charging_data.return_value = None

    # Create a mock dataframe for station data
    mock_repo.dataframe = pd.DataFrame({
        'PLZ': [10116, 10117, 10118],
        'Station': ['Station A', 'Station B', 'Station C']
    })

    return mock_repo


# Test case 1: Postal code found, stations returned
def test_get_stations_found(mock_station_repository):
    # Initialize SearchService with a valid postal code
    service = SearchService(plz=10116)

    # Mock the ChargingStationEvents' behavior
    service.charging_station_service.find_by_post_code = MagicMock(
        return_value=service.charging_station_service.stations_df)

    # Call the method and get the stations
    result = service.get_stations()

    # Assert the correct data is returned
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert not result['PLZ'].empty  # The postal code should match the query


# Test case 3: Empty dataframe, handle error
def test_get_stations_empty_df(mock_station_repository):
    # Initialize SearchService with a valid postal code
    service = SearchService(plz=10116)

    # Simulate an empty dataframe scenario
    service.charging_station_service.stations_df = pd.DataFrame()

    # Call the method
    result = service.get_stations()

    # Ensure that the response is the expected error message for an empty result
    assert result == "Stations for postal code 10116 not found!"


# Test case 4: Handling invalid postal code length
def test_invalid_postal_code_length():
    # Initialize SearchService with an invalid postal code (less than 5 digits)
    plz=9999
    with pytest.raises(ValueError, match="Invalid postal code: {}. Postal code must have 5 digits.".format(plz)):
        service = SearchService(plz=9999)
        service.get_stations()


# Test case 5: Invalid postal code range
def test_invalid_postal_code_range():
    # Initialize SearchService with an invalid postal code (out of valid range)
    with pytest.raises(ValueError, match="PLZ must be between 10115 and 14200"):
        service = SearchService(plz=15000)
        service.get_stations()
