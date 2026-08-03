import pytest
import pandas as pd
from src.Station_search.Domain.entities.entities import Postalcode
from src.Station_search.Domain.events.station_search_events import ChargingStationEvents  # Replace with your actual module


@pytest.fixture
def setup_data():
    # Set up a mock DataFrame for stations
    data = {
        'PLZ': [10116, 10117, 10118],
        'Station': ['Station A', 'Station B', 'Station C']
    }
    stations_df = pd.DataFrame(data)
    return stations_df


def test_valid_postal_code(setup_data):
    postal_code = Postalcode(10116)
    event_service = ChargingStationEvents(postal_code, setup_data)

    # Check if DataFrame is filtered based on the postal code
    filtered_stations = event_service.find_by_post_code()
    assert filtered_stations.shape[0] == 1  # Expecting only one row for PLZ 10116


def test_empty_dataframe():
    postal_code = Postalcode(10116)
    empty_df = pd.DataFrame()  # Empty DataFrame
    event_service = ChargingStationEvents(postal_code, empty_df)

    # Check for empty DataFrame exception
    with pytest.raises(ValueError, match="The input DataFrame is empty."):
        event_service.find_by_post_code()


def test_invalid_postal_code_length():
    # Create Postalcode object with invalid length (not 5 digits)
    postal_code = Postalcode(123)
    event_service = ChargingStationEvents(postal_code, pd.DataFrame())

    # Check for postal code length exception
    with pytest.raises(ValueError, match="Invalid postal code: {}. Postal code must have 5 digits.".format(123)):
        event_service.find_by_post_code()


def test_valid_postal_code_no_match(setup_data):
    # Create Postalcode object with valid postal code but no match in DataFrame
    postal_code = Postalcode(10119)  # Valid but not in the stations_df
    event_service = ChargingStationEvents(postal_code, setup_data)

    # Check for empty DataFrame result
    filtered_stations = event_service.find_by_post_code()
    assert filtered_stations.empty


def test_postal_code_in_dataframe(setup_data):
    # Create Postalcode object with a postal code that exists in the DataFrame
    postal_code = Postalcode(10116)
    event_service = ChargingStationEvents(postal_code, setup_data)

    # Check if the correct row is returned
    filtered_stations = event_service.find_by_post_code()
    assert filtered_stations.shape[0] == 1
    assert filtered_stations.iloc[0]['PLZ'] == 10116
    assert filtered_stations.iloc[0]['Station'] == 'Station A'
