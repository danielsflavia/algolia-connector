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

## Available Endpoints

| Endpoint Path              | Description                      |
|----------------------------|----------------------------------|
| `/top`                     | Top Searches                     |
| `/top/schema`              | Schema for Top Searches          |
| `/count`                   | Total Search Count               |
| `/count/schema`            | Schema for Search Count          |
| `/noresults`               | Searches with No Results         |
| `/noresults/schema`        | Schema for No Results            |
| `/noclicks`                | Searches with No Clicks          |
| `/noclicks/schema`         | Schema for No Clicks             |
| `/clickposition`           | Click Position Data              |
| `/clickposition/schema`    | Schema for Click Position        |
| `/clickthroughrate`        | Click-Through Rate (Daily)       |
| `/clickthroughrate/schema` | Schema for Click-Through Rate    |
| `/userscount`              | Number of Unique Users (Daily)   |
| `/userscount/schema`       | Schema for Users Count           |
| `/countries`               | Top Countries                    |
| `/countries/schema`        | Schema for Top Countries         |
| `/filter`                  | Top Filter Attributes            |
| `/filter/schema`           | Schema for Filter Attributes     |

Start with [Metrics Overview](./metrics-overview.md).
Explore a specific metric in [docs/metrics/](./metrics).