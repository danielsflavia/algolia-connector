# Users Count

## Description

Returns the number of **unique users** per day within a selected time range.  
This is a time-based metric, showing how many different users performed searches each day.

The data for this metric can be retrieved using the `get_users_count()` function  
from [`algolia_connector.py`](../../algolia_connector.py).

## Field description:

| Field     | Description                                               |
|-----------|-----------------------------------------------------------|
| `date`    | Day on which the users were active (format: `YYYY-MM-DD`) |
| `count`   | Number of unique users active on that day                 |

## Schema

```json
{
  "tableName": "algolia_users_count",
  "primaryKey": "date",
  "columns": [
    { "name": "date",  "dataType": "string"  },
    { "name": "count", "dataType": "integer" }
  ]
}
```
> Schema returned by `get_users_count_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).

## How to Analyze

This metric is useful for understanding user behavior and traffic trends:

| Insight                      | Metric/Field | Description                                                  |
|------------------------------|--------------|--------------------------------------------------------------|
| Daily active users           | `count`      | Track how many unique users were active per day             |
| Trend detection              | `count`      | Monitor user growth or drop-off over time                   |
| Correlation with engagement  | JOIN with CTR or search traffic | See if more users result in more clicks or more searches |

## Joins

`Users Count` can be joined with other date-based metrics using the `date` field:

| Related Metric         | Join Key | Available Fields            | Purpose                                      |
|------------------------|----------|-----------------------------|----------------------------------------------|
| `Search Count`         | `date`   | `count`                     | Compare number of users with search volume   |
| `Click Through Rate`   | `date`   | `rate`, `clickCount`        | Track how user count relates to engagement   |
| `No Result Rate`       | `date`   | `rate`, `noResultCount`     | See if failed searches impact user behavior  |

> `Users Count` **cannot** be joined with search-level metrics like `Top Searches`, which do not include a `date` field.
 
