# Top Countries

## Description

Returns the most common **user countries** detected via IP geolocation across all searches.  
This metric shows the geographical distribution of users.

The data for this metric can be retrieved using the `get_top_countries()` function  
from [`algolia_connector.py`](../../algolia_connector.py).

## Field description:

| Field      | Description                            |
|------------|----------------------------------------|
| `country`  | ISO country code of the user           |
| `count`    | Number of users from that country      |

## Schema

```json
{
  "tableName": "algolia_top_countries",
  "primaryKey": "country",
  "columns": [
    { "name": "country", "dataType": "string" },
    { "name": "count",   "dataType": "integer" }
  ]
}
```

## How to Analyze

This metric gives insights into where your users are located:

| Insight                  | Metric/Field | Description                                      |
|--------------------------|--------------|--------------------------------------------------|
| Global distribution      | `country`    | See where most users are coming from             |
| Market share by region   | `count`      | Compare engagement across countries              |

## Joins

`Top Countries` is not directly joinable with other metrics.  
It’s an aggregate metric without a `date` or `search` field.
