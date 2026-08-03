
from src.Issues_report.Domain.entities.report import Issue
class CreateReportEvent:
    def __init__(self, plz: int, report_description :str, station_id : int):
        self.issue = Issue(plz, report_description, station_id)
        self.issue_instance = {}

    def generate_issue_event(self):
        self.issue.validate_plz()
        self.issue.validate_station_id()
        self.issue.validate_description()

        self.issue_instance = {
                    'plz': self.issue.plz,
                    'description': self.issue.description,
                    'station_id': self.issue.station_id,
                 }






