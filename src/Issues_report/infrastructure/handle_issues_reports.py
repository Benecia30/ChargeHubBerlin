import pandas as pd


class IssuesHandler:
    def __init__(self,issue_instance : dict):
        self.issue_instance : dict = issue_instance
        self.issues_dframe = None
        self._path = f"src/Issues_report/infrastructure/report_repository/reports.csv"

    def load_issues_data(self):
        # Load issues data from the Issues_report module
        self.issues_dframe = pd.read_csv(self._path)

    def submit_issue(self):
        # Submit issue data to the Issues_report module
        self.issues_dframe.loc[len(self.issue_instance)-1]=self.issue_instance
        self.issues_dframe.to_csv(self._path, index=False)

