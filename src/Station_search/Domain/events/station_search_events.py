from src.Station_search.Domain.entities.entities import Postalcode
import pandas as pd
class ChargingStationEvents:
    """
    This service is responsible for managing and retrieving charging stations data.
    """
    def __init__(self,postal_code : Postalcode,stations : pd.DataFrame):
        self.plz = postal_code
        self.stations_df = stations

    def find_by_post_code(self):

        self.plz.check_length()

        # Raise exception if the input DataFrame is empty
        if self.stations_df.empty:
            raise ValueError("The input DataFrame is empty.")

        self.plz.check_range()

        if self.plz.plz in self.stations_df["PLZ"].values:
            self.stations_df = self.stations_df[self.stations_df["PLZ"] == self.plz.plz]
        else:
            self.stations_df = pd.DataFrame()  # Set to empty DataFrame if no match

        return self.stations_df