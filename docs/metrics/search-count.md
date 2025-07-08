# Search Count

## Description

Returns the total number of searches per day over a selected time range.  
This is a **time series metric**, meaning each entry includes a specific date and the number of searches executed on that day.

The data for this metric can be retrieved using the `get_searches_count()` function  
from [`algolia_connector.py`](../../algolia_connector.py).

## Field Description

| Field     | Description                                                           |
|-----------|-----------------------------------------------------------------------|
| `date`    | Day on which the searches occurred (format: `YYYY-MM-DD`)            |
| `count`   | Total number of search queries executed on that date (all users)     |


## Schema

```json
{
  "tableName": "algolia_searches_count",
  "primaryKey": "date",
  "columns": [
    { "name": "date",  "dataType": "string"  },
    { "name": "count", "dataType": "integer" }
  ]
}
```
> Schema returned by `get_searches_count_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).

## How to Analyze

The `Search Count` metric is key for tracking usage over time and identifying patterns in search activity:

| Insight                    | Metric/Field | Description                                                     |
|----------------------------|--------------|-----------------------------------------------------------------|
| Search activity trend      | `count`      | Track total search volume across time                           |
| Peak and low traffic days  | `count`      | Identify unusually high or low activity                         |
| Growth monitoring          | `count`      | Compare volume week-over-week, month-over-month, etc.          |
| Seasonal usage patterns    | `date`       | Visualize usage around events, campaigns, or holidays           |
| Engagement correlation     | JOIN with `CTR`, `No Result Rate`, or `Users Count` | Contextualize engagement based on traffic volume  |


## Joins

`Search Count` can be joined with other time-based metrics using the `date` field:

| Related Metric         | Join Key | Fields Available           | Purpose                                                   |
|------------------------|----------|----------------------------|-----------------------------------------------------------|
| `Click Through Rate`   | `date`   | `clickThroughRate`, `count`| Compare clicks to overall traffic                         |
| `No Result Rate`       | `date`   | `rate`, `noResultCount`    | Understand failure rates in context of search volume      |
| `Users Count`          | `date`   | `count`                    | Explore user activity relative to search frequency        |

> `Search Count` **cannot** be joined directly with `Top Searches` or other search-level metrics because it does not include a `search` field.

