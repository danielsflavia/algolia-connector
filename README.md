# Algolia Analytics Connector

The **Algolia Analytics Connector** is a local tool that exposes real-time insights from the [Algolia Analytics API](https://www.algolia.com/doc/rest-api/analytics/).  
It offers both a JSON API and a simple HTML index page, along with a Polars-based analytics layer for deeper exploration.

## Features

- Live Algolia search and click metrics via HTTP endpoints
- Automatic schema inference for each metric
- Polars integration for analysis, aggregation, and visualization
- Simple local server, no web frontend or dashboard required

 ## Quickstart

1. Clone the repo:
   ```bash
   git clone https://github.com/yourname/algolia-connector.git
   cd algolia-connector
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure your environment
    ```bash
    cp .env.example .env
    ```
4. Start the server
    ```bash
    python algolia_connector.py
    ```

## Documentation

| Thema                         | Link                                                               |
|-------------------------------|--------------------------------------------------------------------|
| Setup & Configuration         | [`docs/setup.md`](./docs/setup.md)                                 |
| Metric Endpoints (Übersicht)  | [`docs/metric-endpoints.md`](./docs/metric-endpoints.md)           |
| In-depth Metrics              | [`docs/metrics/`](./docs/metrics/)                                 |
| Polars Analysis Example       | [`polars_test.py`](./polars_test.py)                               |

## Query Parameters (Optional Filters)

All endpoints support optional query parameters:

- `startDate`: Start of range (e.g. `2024-07-01`)
- `endDate`: End of range (e.g. `2024-07-08`)
- `limit`: Max number of items (default: 10)
- `offset`: Pagination offset
- `tags`: Filter using metadata (e.g. `tags=device:mobile phone`)

See full query guide → [`docs/query-parameters.md`](./docs/query-parameters.md)