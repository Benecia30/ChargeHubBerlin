from src.Issues_report.Domain.entities.report import Issue
from src.Issues_report.infrastructure.handle_issues_reports import IssuesHandler
from src.Issues_report.Domain.events.create_report_event import CreateReportEvent

class IssuesReportService:
    """
    This service is responsible for generating reports on issues related to charging stations.
    """
    def __init__(self,plz,report_description,station_id):
        self.current_report = CreateReportEvent(plz,report_description,station_id)


    def submit_report(self):
        self.current_report.generate_issue_event()
        add_issue = IssuesHandler(self.current_report.issue_instance)
        add_issue.load_issues_data()
        add_issue.submit_issue()
