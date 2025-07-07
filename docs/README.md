#  Algolia Connector Documentation

Welcome to the documentation for the Algolia Analytics Connector.

This project provides:
- A local HTTP server exposing live Algolia metrics
- Structured schema generation for each metric
- Polars-based data transformation
- Ready-to-use analysis and insights

To run locally:
```bash
python algolia_connector.py
```
Server runs at: http://localhost:8000/

- See the [Metrics Overview](./metrics-overview.md).
- All available HTTP endpoints are listed in [Available Endpoints](./endpoints.md).
- For detailed metric documentation, check the pages in [docs/metrics/](./metrics/).