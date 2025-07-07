#  Algolia Connector Documentation

Welcome to the documentation for the **Algolia Analytics Connector**.

This project provides:
- A local HTTP server exposing live [Algolia](https://www.algolia.com/) metrics
- Structured schema generation for each metric
- Polars-based data transformation
- Ready-to-use analysis and insights

> You'll need an [Algolia Analytics API key](https://www.algolia.com/doc/rest-api/analytics/#analytics-api-keys) and application ID to connect.

To run locally:
```bash
python algolia_connector.py
```
Server runs at: http://localhost:8000/

- See [Metric Endpoints](./metric-endpoints.md) for a full list of metrics and their API routes.  
- Explore each metric in detail in [docs/metrics/](./metrics/).
