# Available Endpoints

This page lists all HTTP endpoints exposed by the Algolia Connector.  
Each endpoint returns **raw data** or a **structured schema**, and links to a corresponding documentation page for context and analysis.

## Search Metrics

| Endpoint                | Returns                           | Documentation                      |
|------------------------|------------------------------------|-------------------------------------|
| `/top`                 | Most frequent search queries       | [Top Searches](./metrics/top-searches.md) |
| `/top/schema`          | Schema for top searches            | —                                   |
| `/count`               | Search count over time             | [Search Count](./metrics/search-count.md) |
| `/count/schema`        | Schema for search count            | —                                   |
| `/noresults`           | Searches with no results           | [No Results](./metrics/no-results.md) |
| `/noresults/schema`    | Schema for no results              | —                                   |
| `/norate`              | Daily no-result rate               | *not yet documented*                |
| `/norate/schema`       | Schema for no-result rate          | —                                   |


## Click Metrics

| Endpoint                | Returns                               | Documentation             |
|------------------------|----------------------------------------|----------------------------|
| `/noclicks`            | Searches that didn't result in a click | *not yet documented*       |
| `/noclicks/schema`     | Schema for no clicks                   | —                          |
| `/clickposition`       | Position of user clicks                | *not yet documented*       |
| `/clickposition/schema`| Schema for click positions             | —                          |
| `/clickthroughrate`    | Daily click-through rates              | *not yet documented*       |
| `/clickthroughrate/schema` | Schema for CTR                   | —                          |


## User Metrics

| Endpoint                | Returns                               | Documentation             |
|------------------------|----------------------------------------|----------------------------|
| `/userscount`          | Unique user count per day              | *not yet documented*       |
| `/userscount/schema`   | Schema for user count                  | —                          |
| `/countries`           | Top user countries                     | *not yet documented*       |
| `/countries/schema`    | Schema for top countries               | —                          |


## Filter Usage

| Endpoint                | Returns                               | Documentation             |
|------------------------|----------------------------------------|----------------------------|
| `/filter`              | Most used filters (by attribute)       | *not yet documented*       |
| `/filter/schema`       | Schema for filter attributes           | —                          |


> Use the `/schema` endpoints to inspect available fields, data types, and primary keys for joining metrics in Polars or SQL-like analysis.
