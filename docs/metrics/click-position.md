# Click Positions

## Description

Returns the **positions** within the result list that users clicked on.  
Useful for analyzing ranking effectiveness and scroll behavior.

The data for this metric can be retrieved using the `get_click_positions()` function  
from [`algolia_connector.py`](../../algolia_connector.py).

## Field Description

| Field         | Description                                             |
|---------------|---------------------------------------------------------|
| `position`    | Clicked result rank (0-indexed) or position bin         |
| `clickCount`  | Total number of clicks at this position or range        |

## Schema

```json
{
  "tableName": "algolia_click_positions",
  "primaryKey": "position",
  "columns": [
    { "name": "position",   "dataType": "list<int>" },
    { "name": "clickCount", "dataType": "integer" }
  ]
}
```
> Schema returned by `get_click_positions_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).

## How to Analyze

Click Positions reveal how deep users scroll in search results before clicking:

| Insight                         | Metric/Field   | Description                                                              |
|----------------------------------|----------------|-------------------------------------------------------------------------|
| User scroll depth               | `position`     | Analyze the index positions where users tend to click                    |
| Result relevance                | `position`     | More clicks on top positions suggest good relevance ranking              |
| Engagement hotspots             | `clickCount`   | Identify which result positions get the most interaction                 |
| Interaction distribution        | `clickCount` + `position` | Build a histogram of click behavior across result ranks       |
| Outlier patterns                | `position`     | Detect when users frequently click deep in the result list               |

## Joins

`Click Positions` is **not directly joinable** with search- or date-based metrics.

- It does not include a `search` or `date` field.
- The `position` field reflects result ranks globally (aggregated across all queries).
