# Top Filter Attributes

## Description

Returns the most commonly used filter attributes (facets) applied by users during search interactions.  
This metric helps identify which filters are most relevant or frequently interacted with.

The data for this metric can be retrieved using the `get_top_filter_attributes()` function  
from [`algolia_connector.py`](../../algolia_connector.py).


## Field Description

| Field       | Description                                           |
|-------------|-------------------------------------------------------|
| `attribute` | Name of the filter attribute (facet)                 |
| `count`     | Number of times this attribute was used as a filter  |

## Schema

```json
{
  "tableName": "algolia_top_filter_attributes",
  "primaryKey": "attribute",
  "columns": [
    { "name": "attribute", "dataType": "string" },
    { "name": "count",     "dataType": "integer" }
  ]
}
  ```
> Schema returned by `get_top_filter_attributes_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).

## How to Analyze

| Insight                        | Field       | Description                                                        |
|--------------------------------|-------------|--------------------------------------------------------------------|
| Most used filters              | `attribute` | See which filters users engage with most often                    |
| Refinement popularity          | `count`     | Identify which attributes drive segmentation and refinement       |
| Filter UI optimization         | `attribute` | Use top attributes to prioritize placement in the UI              |

## Joins

`Top Filter Attributes` is typically analyzed independently.

- It contains aggregate counts per attribute name, not tied to a `search`, `date`, or `user`.
- For deeper insight, you can **map `attribute` values** to your schema or taxonomy to group filters (e.g. brand vs. color).

> This metric is **not directly joinable** with other metrics, but complements them for UI and behavior insights.