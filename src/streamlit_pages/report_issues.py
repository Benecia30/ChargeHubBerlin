import streamlit as st

from src.Issues_report.Application.stations_issues_report_service import IssuesReportService

def submit_report(issue_description, postal_code, station_id):
    # Handle the complaint submission logic here
    st.success("Complaint submitted successfully!")

    report_service = IssuesReportService(postal_code,issue_description, station_id)
    report_service.submit_report()

    st.write("### Submitted Details")

    st.write(f"**Postal Code:** {postal_code}")
    st.write(f"**Station ID:** {station_id}")
    st.write(f"**Issue Description:** {issue_description}")


    reset = st.form_submit_button("Reset Form", on_click=reset_form)

def reset_form():
    st.session_state.station_id = None
    st.session_state.postal_code = None
    st.session_state.issue_text = ""

def display_report_window():

    postal_dict = {
            10115: list(range(1, 28)) ,
            10117:  list(range(1, 55)) ,
            10119: list(range(1, 7)) ,
            10177: [1],
            10178: list(range(1, 31)) ,
            10179: list(range(1, 38)) ,
            10243: list(range(1, 40)) ,
            10245: list(range(1, 17)) ,
            10247: list(range(1, 14)) ,
            10249: list(range(1, 29)) ,
            10315: list(range(1, 7)) ,
            10317: list(range(1, 17)) ,
            10318: list(range(1, 5)) ,
            10319: list(range(1, 6)) ,
            10365: list(range(1, 19)) ,
            10367: list(range(1, 6)) ,
            10369: list(range(1, 7)) ,
            10405: list(range(1, 12)) ,
            10407: list(range(1, 21)) ,
            10409: list(range(1, 12)) ,
            10435: list(range(1, 7)) ,
            10437: list(range(1, 10)) ,
            10439: list(range(1, 13)) ,
            10551: list(range(1, 6)) ,
            10553: list(range(1, 12)) ,
            10555: list(range(1, 12)) ,
            10557: list(range(1, 61)) ,
            10559: list(range(1, 39)) ,
            10585: [1, 2, 3, 4, 5, 6],
            10587: list(range(1, 36)) ,
            10589: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            10623: list(range(1, 26)) ,
            10625: [1, 2, 3],
            10627: [1, 2, 3, 4],
            10629: [1, 2, 3, 4, 5],
            10707: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            10709: [1, 2, 3, 4, 5, 6, 7, 8],
            10711: [1, 2, 3, 4, 5, 6],
            10713: [1, 2, 3, 4, 5, 6],
            10715: [1, 2, 3, 4, 5, 6],
            10717: [1, 2, 3, 4, 5, 6, 7, 8],
            10719: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            10777: [1, 2, 3, 4, 5, 6, 7],
            10779: [1],
            10781: [1, 2, 3, 4, 5, 6],
            10783: [1, 2, 3],
            10785: list(range(1, 61)) ,
            10787: list(range(1, 22)) ,
            10789: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            10823: [1, 2],
            10825: [1, 2, 3, 4, 5, 6],
            10827: [1, 2, 3, 4, 5],
            10829: list(range(1, 56)) ,
            10936: [1],
            10961: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            10963: list(range(1, 28)) ,
            10965: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            10967: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            10969: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            10997: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            10999: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            12043: [1, 2, 3, 4, 5],
            12045: [1, 2, 3, 4, 5],
            12047: [1, 2, 3, 4, 5, 6, 7],
            12049: [1, 2],
            12051: [1, 2, 3, 4, 5, 6, 7, 8],
            12053: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            12055: [1, 2, 3, 4],
            12057: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            12059: [1, 2, 3, 4, 5, 6, 7],
            12099: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            12101: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            12103: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            12105: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            12107: [1, 2, 3, 4, 5, 6],
            12109: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            12137: [1, 2],
            12154: [1],
            12157: [1, 2, 3, 4, 5],
            12159: [1, 2, 3, 4, 5, 6, 7, 8],
            12161: [1, 2, 3, 4, 5, 6, 7, 8],
            12163: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            12165: [1, 2, 3, 4, 5, 6],
            12167: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            12169: [1, 2, 3, 4, 5, 6, 7, 8],
            12203: list(range(1, 39)) ,
            12205: list(range(1, 30)) ,
            12207: list(range(1, 27)) ,
            12209: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            12247: list(range(1, 24)) ,
            12249: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            12277: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
            12279: [1, 2],
            12305: [1, 2, 3],
            12307: [1, 2],
            12347: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            12349: [1, 2, 3, 4, 5],
            12351: list(range(1, 59)) ,
            12353: [1, 2, 3, 4],
            12355: [1, 2, 3, 4, 5],
            12357: [1, 2, 3, 4],
            12359: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            12435: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            12437: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            12439: list(range(1, 33)) ,
            12459: list(range(1, 25)) ,
            12487: list(range(1, 23)) ,
            12489: list(range(1, 21)) ,
            12524: list(range(1, 22)) ,
            12526: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            12527: [1, 2],
            12555: list(range(1, 26)) ,
            12557: [1, 2, 3, 4, 5, 6, 7, 8],
            12559: [1, 2],
            12587: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            12589: [1, 2],
            12619: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            12621: list(range(1, 35)) ,
            12623: list(range(1, 83)) ,
            12627: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            12629: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            12679: [1, 2, 3, 4, 5, 6],
            12681: list(range(1, 43)) ,
            12683: list(range(1, 96)) ,
            12685: [1, 2, 3, 4, 5, 6, 7, 8],
            12687: [1, 2, 3, 4, 5, 6],
            12689: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            13051: [1, 2, 3, 4, 5],
            13053: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            13054: [1],
            13055: list(range(1, 31)) ,
            13057: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            13059: [1],
            13086: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            13088: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            13089: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            13125: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            13127: [1, 2, 3, 4, 5, 6],
            13156: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            13159: [1],
            13187: [1, 2, 3, 4, 5, 6, 7, 8],
            13189: [1, 2, 3, 4],
            13347: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            13349: [1, 2],
            13351: [1, 2],
            13353: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            13355: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
            13357: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            13359: [1, 2, 3, 4],
            13403: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            13405: [1, 2, 3, 4, 5, 6],
            13407: [1, 2, 3, 4],
            13409: [1, 2, 3, 4, 5, 6, 7],
            13435: [1, 2, 3, 4],
            13437: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            13439: [1],
            13465: list(range(1, 49)),
            13467: list(range(1, 36)) ,
            13469: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            13501: [1],
            13507: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            13509: list(range(1, 32)) ,
            13539: [1, 2],
            13581: list(range(1, 31)) ,
            13583: [1, 2, 3, 4, 5, 6, 7, 8],
            13585: list(range(1, 54)) ,
            13587:list(range(1, 21)) ,
            13589: [1, 2, 3],
            13591: [1, 2, 3, 4, 5, 6],
            13593: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            13595: [1, 2, 3, 4, 5, 6],
            13597: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            13599: list(range(1, 27)),
            13627: [1, 2],
            13629: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            14050: [1, 2, 3, 4, 5, 6, 7],
            14052: [1, 2, 3],
            14055: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            14057: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            14059: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            14089: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            14109: list(range(1, 24)),
            14129: list(range(1, 36)),
            14163: list(range(1, 33)),
            14165: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            14167: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            14169: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            14193: [1, 2, 3],
            14195: list(range(1, 33)),
            14197: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            14199: [1, 2, 3, 4, 5, 6, 7],
            14597: [1],
            14641: [1, 2, 3],
            42329: [1],
            47166: [1, 2]}

    if "station_id" not in st.session_state:
        st.session_state.station_id = None
    if "postal_code" not in st.session_state:
            st.session_state.postal_code = None

    if "issue_text" not in st.session_state:
            st.session_state.issue_text = ""


    # Form layout
    with st.form(key="complaint_form"):
        col1, col2 = st.columns([3, 1])

        # Left column for complaint text area
        with col1:
            st.session_state.issue_text = st.text_area(
                "Write your complaint/issue here:",
                height=200,
                placeholder="Describe your issue...",
                value=st.session_state.issue_text
            )
        # Right column for other details
        with col2:
            st.session_state.postal_code = st.selectbox("Postal Code", list(postal_dict.keys()))
            station_selection = st.form_submit_button("Confirm Station")

            if station_selection:
                st.session_state.station_id = st.selectbox(
                        "Station ID",
                        postal_dict[st.session_state.postal_code]
                )
                st.write("Select", st.session_state.station_id)


        # Submit button
        submitted = st.form_submit_button("Submit Complaint")
        if submitted:

            if not st.session_state.issue_text.strip():
                st.error("Please provide a complaint description.")
            elif not st.session_state.postal_code or not st.session_state.station_id:
                st.error("Please fill in all fields.")
            else:
                submit_report(st.session_state.issue_text, st.session_state.postal_code, st.session_state.station_id)


