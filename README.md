# ⚡ ChargeHub Berlin

A Streamlit application that helps identify where Berlin needs more electric
vehicle charging infrastructure — by combining population data with the
existing charging station network, letting users search stations by postal
code, and collecting user-reported issues about existing stations.

Built as a team project for the **Advanced Software Engineering** module,
applying **Domain-Driven Design (DDD)** and **Test-Driven Development (TDD)**
practices throughout.

## Live Demo

Run locally with:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app opens with three pages: **Charging-Hub** (overview map), **Search**
(look up stations by postal code), and **Report Issue** (flag a problem with
a station).

## Use Cases

1. **Station Search** — look up all charging stations for a given Berlin
   postal code (PLZ), so drivers can quickly find nearby infrastructure.
2. **Issue Reporting** — allow users to report problems with a charging
   station (e.g. broken, occupied, missing), so operators and future users
   have up-to-date, crowdsourced information.

Both use cases sit alongside a shared **Charging** context that loads,
cleans, and geo-enriches the raw datasets that power the map view.

## Data Sources

- **Charging station infrastructure per postal code** — Bundesnetzagentur
  ("Ladesäulenregister")
- **Population per postal code** — [suche-postleitzahl.org](https://www.suche-postleitzahl.org/downloads)
- Berlin postal code / district geometries for the map layer

## Tech Stack

| Purpose | Technology |
|---|---|
| Language | Python |
| Frontend / app framework | Streamlit + `st-pages` (multi-page navigation) |
| Data processing | pandas, GeoPandas |
| Mapping | Folium, `streamlit-folium`, Shapely, pyproj |
| Testing | pytest, pytest-cov |
| Linting / formatting | pylint, mypy, black, isort |

## Architecture

The codebase follows **Domain-Driven Design**, organized into bounded
contexts, each split into `Domain`, `Application`, and `infrastructure`
layers:

```
src/
├── Charging/            # Loads & geo-preprocesses raw station + population data
│   ├── Domain/           # Entities (GeoData, Station) and geo services
│   ├── Application/       # Geo preprocessing orchestration
│   └── infrastructure/    # CSV loading, config
│
├── Station_search/       # Use case: search stations by postal code
│   ├── Domain/            # Postalcode entity, ChargingStationEvents, repository interface
│   ├── Application/       # SearchService
│   └── infrastructure/    # Repository implementation, config
│
├── Issues_report/         # Use case: report a station issue
│   ├── Domain/            # Report entity, report-created event
│   ├── Application/       # Issue report service
│   └── infrastructure/    # Persistence for reports
│
├── Shared/                 # Shared datasets used across contexts
│   └── infrastructure/datasets/
│
└── streamlit_pages/         # UI layer (one file per page), wired up in app.py
```

Each context keeps its domain logic (entities, events, business rules)
independent of how data is loaded or how it's rendered — `infrastructure`
handles I/O (CSV loading, repositories), `Application` orchestrates use
cases, and `streamlit_pages` is a thin UI layer on top.

## Testing

Tests live under `tests/`, mirrored by bounded context (`Station_search/`,
`Issues_report/`), and were written test-first for the domain logic (e.g.
postal code validation, station filtering, empty-data handling). Run them
with:

```bash
pytest --cov=src
```

## Project Status

Core use cases (station search, issue reporting, and the overview map) are
implemented and working end-to-end. Possible next steps include expanding
test coverage to the `Charging` context and adding per-kW map layers.

## Team

Built collaboratively as part of a university group project as a team of 4 people. 

## License

MIT — see [LICENSE](LICENSE).
