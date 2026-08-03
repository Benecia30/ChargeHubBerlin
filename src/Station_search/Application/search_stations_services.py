from src.Station_search.Domain.events.station_search_events import ChargingStationEvents
from src.Station_search.infrastructure.charging_station_repository import  ChargingRepository
from src.Station_search.Domain.entities.entities import Postalcode


class SearchService:

    def __init__(self,plz:int):

        self.postal_code = Postalcode(plz)  # Intialization of postal code entity with plz (Postal code)
        self.station_repo = ChargingRepository()  # Intialization of ChargingStationRepository to get the station data
        self.station_repo.load_charging_data() # Load the station data
        self.charging_station_service = ChargingStationEvents(self.postal_code,self.station_repo.dataframe) # Get postal code stations


    def get_stations(self):

        if self.charging_station_service.stations_df.empty:
            return "Stations for postal code 10116 not found!"

        self.charging_station_service.find_by_post_code()



        if self.charging_station_service.stations_df.empty:
            return "Stations for postal code {} not found!".format(self.postal_code.plz)
        else:
            return self.charging_station_service.stations_df
