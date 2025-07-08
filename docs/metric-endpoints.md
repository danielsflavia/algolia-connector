# Metric Endpoints

This page lists all HTTP endpoints exposed by the Algolia Connector.  
Each endpoint returns **raw data** and a **structured schema**, and links to a corresponding documentation page for context and analysis.

## Search Metrics

| Metric           | Endpoints                                   | Documentation                               |
|------------------|---------------------------------------------|---------------------------------------------|
| Top Searches     | [`/top`](#), [`/top/schema`](#)             | [Top Searches](./metrics/top-searches.md)   |
| Search Count     | [`/count`](#), [`/count/schema`](#)         | [Search Count](./metrics/search-count.md)   |
| No Results       | [`/noresults`](#), [`/noresults/schema`](#) | [No Results](./metrics/no-results.md)       |
| No Result Rate   | [`/norate`](#), [`/norate/schema`](#)       | [No Result Rate](./metrics/no-result-rate.md)|
| Top Hits         | [`/hits`](#), [`/hits/schema`](#)           | [Top Hits](./metrics/top-hits.md)           |


## Click Metrics

| Metric               | Endpoints                                           | Documentation                                              |
|----------------------|-----------------------------------------------------|------------------------------------------------------------|
| No Clicks            | [`/noclicks`](#), [`/noclicks/schema`](#)           |[No Clicks](./metrics/no-clicks.md)                         |
| Click Positions      | [`/clickposition`](#), [`/clickposition/schema`](#) | [Click Positions](./metrics/click-position.md)             |
| Click Through Rate   | [`/clickthroughrate`](#), [`/clickthroughrate/schema`](#)| [Click Through Rate](./metrics/click-through-rate.md) |

## User Metrics

| Metric           | Endpoints                                       | Documentation                |
|------------------|-------------------------------------------------|------------------------------|
| Users Count      | [`/userscount`](#), [`/userscount/schema`](#)   | _Not yet documented_         |
| Top Countries    | [`/countries`](#), [`/countries/schema`](#)     | _Not yet documented_         |

## Filter Usage

| Metric                 | Endpoints                                     | Documentation                |
|------------------------|-----------------------------------------------|------------------------------|
| Top Filter Attributes  | [`/filter`](#), [`/filter/schema`](#)         | _Not yet documented_         |

> Use the `/schema` endpoints to inspect available fields, data types, and primary keys for joining metrics in Polars or SQL-like analysis.
