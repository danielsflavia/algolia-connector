# No results

## Description

Returns individual search queries that resulted in **zero hits** during the selected time range.  
Useful for identifying content gaps and opportunities to improve search relevance or indexing.

The data for this metric can be retrieved using the `get_searches_no_results()` function  
from [`algolia_connector.py`](../../algolia_connector.py)


## Field description:

| Field               | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `search`            | The original search query entered by the user                               |
| `count`             | Number of times this query was executed and returned **no results**         |
| `withFilterCount`   | Number of times this query returned no results while a filter was applied   |

## Schema

```json
{
  "tableName": "algolia_searches_no_results",
  "primaryKey": "search",
  "columns": [
    { "name": "search",           "dataType": "string"  },
    { "name": "count",            "dataType": "integer" },
    { "name": "withFilterCount",  "dataType": "integer" }
  ]
}
```

> Schema returned by `get_searches_no_results_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).

## How to Analyze

| Insight                          | Metric             | Description                                                                 |
|---------------------------------|---------------------|-----------------------------------------------------------------------------|
| Identify unserved user intent   | `search`, `count`  | Most common queries that returned zero results                              |
| Filter-induced result loss      | `withFilterCount`  | Spot where filters cause result suppression                                 |
| Content gap diagnosis           | `search`           | Compare to indexed content or product data                                  |
| Prioritization for content fixes| `count`            | Higher counts indicate more urgent opportunities for improvement            |

## Joins

You can join **No Results** with other search-level metrics using `search` as the join key:

| Related Metric        | Join Key | Fields Available        | Purpose                                                             |
|-----------------------|----------|--------------------------|---------------------------------------------------------------------|
| `Top Searches`        | `search` | `count`, `clickCount`    | Find top queries that return no results                             |
| `Searches No Clicks`  | `search` | `count`                  | See if failed queries also lead to no user interaction              |
