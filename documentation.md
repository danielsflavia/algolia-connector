## Algolia Metrics 

This document describes the key metrics available from the `algolia_connector`, along with their associated schema definitions. The data is processed using Polars, with clearly typed columns for consistent usage across analytics pipelines.

### 1. Top Searches

#### Description
This metric returns the most frequently executed search queries within a given time range.
It includes how often a search was performed, how many results it returned, and how often users interacted with it (clicked, converted, etc.).

#### Breakdown / How to interpret

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


#### Schema

```json
{
  "tableName": "algolia_top_searches",
  "primaryKey": "search",
  "columns": [
    { "name": "search",               "dataType": "string"       },
    { "name": "count",                "dataType": "integer"      },
    { "name": "nbHits",               "dataType": "integer"      },
    { "name": "averageClickPosition", "dataType": "float"        },
    { "name": "clickCount",           "dataType": "integer"      },
    { "name": "clickPositions",       "dataType": "json"         },
    { "name": "clickThroughRate",     "dataType": "float"        },
    { "name": "conversionCount",      "dataType": "integer"      },
    { "name": "conversionRate",       "dataType": "integer"      },
    { "name": "trackedSearchCount",   "dataType": "integer"      }
  ]
}
```
> **Note**:  
> The field `clickPositions` is originally a list of objects like  
> `[{"position": 1, "count": 7}, {"position": 2, "count": 3}]`,  
> but it is serialized to a JSON string in the DataFrame.  
> You can parse it using `json.loads(row["clickPositions"])` if needed.