# Top Searches

## Description

Returns the most popular search queries for the selected time range.  

The data for this metric can be retrieved using the `get_top_searches()` function  
from [`algolia_connector.py`](../../algolia_connector.py).

## Field description:

| Field                    | Description                                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------|
| `search`                 | Raw search term entered by users                                                                               |
| `count`                  | Total number of times this query was executed (includes searches with `clickAnalytics=false`)                  |
| `nbHits`                 | Average number of results (hits) returned for this query                                                       |
| `averageClickPosition`   | Mean position of the clicked result (1 = first result)                                                         |
| `clickCount`             | Number of clicks recorded for this query *(only if `clickAnalytics=true`)*                                     |
| `clickPositions`         | JSON-encoded list of positions clicked and their click counts                                                  |
| `clickThroughRate`       | `clickCount / trackedSearchCount` (CTR)                                                                        |
| `conversionCount`        | Number of conversions recorded for this query *(requires conversion events in Algolia)*                        |
| `conversionRate`         | `conversionCount / trackedSearchCount`                                                                         |
| `trackedSearchCount`     | Number of searches where **`clickAnalytics=true`** (basis for CTR and conversion rate)                         |

> **Requires** `clickAnalytics=true` in the API request to include click and conversion metrics such as `clickCount`, `conversionRate`, etc.


## Schema

```json
{
  "tableName": "algolia_top_searches",
  "primaryKey": "search",
  "columns": [
    { "name": "search",               "dataType": "string"  },
    { "name": "count",                "dataType": "integer" },
    { "name": "nbHits",               "dataType": "integer" },
    { "name": "averageClickPosition", "dataType": "float"   },
    { "name": "clickCount",           "dataType": "integer" },
    { "name": "clickPositions",       "dataType": "json"    },
    { "name": "clickThroughRate",     "dataType": "float"   },
    { "name": "conversionCount",      "dataType": "integer" },
    { "name": "conversionRate",       "dataType": "integer" },
    { "name": "trackedSearchCount",   "dataType": "integer" }
  ]
}
```

> Schema returned by `get_top_searches_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).


## How to Analyze

This metric is useful for evaluating both query popularity and user engagement with results:

| Insight                           | Metric                           | Description                                                                 |
|----------------------------------|------------------------------------|-----------------------------------------------------------------------------|
| Most popular searches            | `search`, `count`                  | Raw query volume                                                            |
| Result volume                    | `nbHits`                           | Detect over-saturated (many hits) or under-supplied queries                |
| Engagement with results          | `clickCount`, `clickThroughRate`  | Identify whether users click results after searching                        |
| Click depth                      | `averageClickPosition`             | Detect how deep users scroll for clicks (lower = better relevance)         |
| Conversion potential             | `conversionCount`, `conversionRate` | Evaluate which queries lead to actual conversions                         |
| Behavior of high-volume queries  | JOIN with `Searches No Clicks` or `No Results` | Understand drop-off or failure points                          |

## Joins

`Top Searches` can be joined with other search-level metrics using the `search` field as a common key:

| Related Metric           | Join Key | Fields Available                     | Purpose                                                             |
|--------------------------|----------|--------------------------------------|---------------------------------------------------------------------|
| `Searches No Results`    | `search` | `count`                              | Check which top searches return no results                          |
| `Searches No Clicks`     | `search` | `count`                              | See which queries don't result in any clicks                        |
| `Click Positions`        | `search` | `position`, `clickCount`             | Analyze which position(s) users clicked on for each search query   |

> `Top Searches` **cannot** be joined with time-based metrics like `Search Count`, `Click Through Rate`, or `Users Count` because it doesn't include a `date` field.
