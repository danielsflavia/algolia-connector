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
```

## How to Analyze

You can break down `Top Searches` by:

- **Time**: Join or group by date using the `trackedSearchCount` from the [Click Through Rate](./click-through-rate.md) metric.
- **Click Behavior**: Use `clickPositions` to understand where users clicked (e.g. top-ranked or buried results).
- **Conversion Funnel**: Analyze `clickCount`, `clickThroughRate`, and `conversionRate` together to evaluate effectiveness.
- **No-Result Overlay**: Cross-reference with the [No Results](./no-results.md) metric to check if a query is failing for some users.


## Related Metrics & Joins

This metric can be joined with others using:

| Join Target                    | Join Key   | Purpose                                               |
|-------------------------------|------------|--------------------------------------------------------|
| [Click Through Rate](./click-through-rate.md) | `search` | Combine CTR data by query                |
| [No Results](./no-results.md)              | `search` | See if queries often lead to empty results  |
| [Search Count](./search-count.md)          | `date`   | Add temporal search volume to query metrics |

Use `.join()` in Polars or SQL-like environments to combine those metrics based on `search` or `date`.
