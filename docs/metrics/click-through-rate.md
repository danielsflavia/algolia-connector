# Click Through Rate (CTR)

## Description

Returns the **click-through rate** (CTR) per day:  
The percentage of tracked searches (`clickAnalytics=true`) that resulted in at least one click.

The data for this metric can be retrieved using the `get_click_through_rate()` function  
from [`algolia_connector.py`](../../algolia_connector.py)

## Field Description

| Field                 | Description                                                                 |
|------------------------|----------------------------------------------------------------------------|
| `date`                | Day of measurement (UTC)                                                    |
| `clickCount`          | Total number of clicks recorded on this day                                |
| `trackedSearchCount`  | Number of tracked searches (`clickAnalytics=true`)                          |
| `rate`                | CTR = `clickCount / trackedSearchCount`                                    |

## Schema

```json
{
  "tableName": "algolia_click_through_rate",
  "primaryKey": "date",
  "columns": [
    { "name": "rate",                "dataType": "float" },
    { "name": "clickCount",         "dataType": "integer" },
    { "name": "trackedSearchCount", "dataType": "integer" },
    { "name": "date",               "dataType": "string" }
  ]
}
```
> Schema returned by `get_click_through_rate_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).

## How to Analyze

Click Through Rate (CTR) is a central indicator of how often users engage with search results:

| Insight                         | Metric/Field     | Description                                                                 |
|----------------------------------|------------------|----------------------------------------------------------------------------|
| Daily engagement trends          | `rate`           | Track CTR over time to detect regressions or improvements                  |
| Activity context                 | `clickCount`     | Raw number of clicks gives insight into volume                             |
| Search tracking completeness     | `trackedSearchCount` | Number of searches with `clickAnalytics=true`                          |
| Performance monitoring           | `rate`           | Compare before/after deployments, campaigns, or content changes            |

## Joins

`Click Through Rate` can be joined with other **date-based metrics** using the `date` field:

| Related Metric         | Join Key | Fields Available              | Purpose                                                   |
|------------------------|----------|-------------------------------|-----------------------------------------------------------|
| `Search Count`         | `date`   | `count`                       | Calculate CTR as a % of total searches                    |
| `No Result Rate`       | `date`   | `rate`, `noResultCount`       | Understand if CTR drops coincide with bad result coverage |
| `Users Count`          | `date`   | `count`                       | Correlate CTR with user activity                          |

> `Click Through Rate` **cannot** be joined with search-level metrics like `Top Searches` or `Searches No Clicks` because it lacks a `search` field.




