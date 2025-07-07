# Top Searches

## Description
Returns the most frequently executed search queries, including click and conversion metrics.

## Field description:

| Field                  | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `search`               | The raw search term entered by users                                        |
| `count`                | Total number of times this search query was executed                        |
| `nbHits`               | Total number of results (hits) returned for this query                      |
| `averageClickPosition`| Mean position of the clicked result (e.g., 1st, 2nd, etc.)                   |
| `clickCount`           | Number of times a user clicked on a result after this search                |
| `clickPositions`       | List of clicked positions and how often each was clicked (stored as JSON)   |
| `clickThroughRate`     | Share of tracked searches that led to a click (`clickCount / trackedSearchCount`) |
| `conversionCount`      | Number of conversions attributed to this search                             |
| `conversionRate`       | Share of tracked searches that led to a conversion                          |
| `trackedSearchCount`   | Number of tracked searches (basis for CTR and conversion rate)              |

> **Note:**  
> The field `clickPositions` contains a list of objects but is stored as a JSON string after processing.  
> You can decode it using `json.loads(row["clickPositions"])`.

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