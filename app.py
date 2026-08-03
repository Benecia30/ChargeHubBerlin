import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
st.set_page_config(layout="wide")


# Style main-container of streamlit application
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;  /* Adjust this value as needed */
            margin-top: 1rem;   /* Adjust this value as needed */
        }
    </style>
""", unsafe_allow_html=True)

# Load all the navigation items into sidebar elements
nav = get_nav_from_toml("pages_sections.toml")

pg = st.navigation(nav) # Store the navigation

add_page_title(pg) # Add the page title


# Render page content based on the selected page
if pg.title == "Charging-Hub":
    # This is the main content page of the Charging-Hub
    from src.streamlit_pages.stations import display_stations
    display_stations() # Show all stations

elif pg.title == "Search":
    # This is the search page of the Charging-Hub
    from src.streamlit_pages.search import display_search
    display_search() # Search for specific postal code stations

elif pg.title == "Report Issue":
    from src.streamlit_pages.report_issues import display_report_window
    display_report_window() # Report issues