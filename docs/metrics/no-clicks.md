# No Clicks

## Description

Returns the search terms that resulted in **no click** on any result.  
These queries indicate potential issues with result quality or user intent mismatch.

The data for this metric can be retrieved using the `get_searches_no_clicks()` function  
from [`algolia_connector.py`](../../algolia_connector.py).

## Field Description

| Field     | Description                                           |
|-----------|-------------------------------------------------------|
| `search`  | Raw query text entered by the user                    |
| `count`   | Number of times this query resulted in no click       |
| `nbHits`  | Average number of results returned for the query      |

## Schema

```json
{
  "tableName": "algolia_searches_no_clicks",
  "primaryKey": "search",
  "columns": [
    { "name": "search", "dataType": "string" },
    { "name": "count",  "dataType": "integer" },
    { "name": "nbHits", "dataType": "integer" }
  ]
}
```
> Schema returned by `get_searches_no_clicks_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).

## How to Analyze

This metric helps reveal search queries that failed to drive any engagement:

| Insight                     | Metric/Field | Description                                                                 |
|----------------------------|--------------|-----------------------------------------------------------------------------|
| Ignored but answerable     | `nbHits`     | Queries returned results, but users didn’t click—possibly poor quality     |
| Zero-engagement patterns   | `search`     | Group queries by theme to identify gaps (e.g., empty intent, UI issues)    |
| Priority issues            | `count`      | Sort by count to focus on most frequent no-click searches                  |

## Joins

`No Clicks` can be joined with other **search-level metrics** using the `search` field:

| Related Metric       | Join Key | Fields Available         | Purpose                                                  |
|----------------------|----------|--------------------------|----------------------------------------------------------|
| `Top Searches`       | `search` | `count`, `clickCount`    | Filter for high-traffic queries with no engagement       |
| `Searches No Results`| `search` | `count`                  | Distinguish between zero-clicks due to zero results      |

> This table **cannot** be joined with time-based metrics like `Search Count` or `Click Through Rate` because it lacks a `date` field.