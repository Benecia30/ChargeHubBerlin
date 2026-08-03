class Issue:

    def __init__(self, plz : int, report_description : str, station_id : int):

        self.plz         : int = plz
        self.description : str = report_description
        self.station_id  : int = station_id


    # Validate the Postal code
    def validate_plz(self):
        if not isinstance(self.plz, int) or len(str(self.plz)) != 5:
            raise ValueError("Invalid postal code. Postal code must be a 5-digit number.")
        return True

    def validate_description(self):
        if not isinstance(self.description, str) or len(self.description) < 10:
            raise ValueError("Invalid report description. Description must be a string with at least 10 characters.")
        return True

    def validate_station_id(self):
        if not isinstance(self.station_id, int):
            raise ValueError("Invalid station ID. Station ID must be an integer.")
        return True
