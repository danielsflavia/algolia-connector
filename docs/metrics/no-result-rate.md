# No Result Rate

## Description

Returns the fraction of searches that didn’t return any results within a time range, including a daily breakdown.  
This metric helps identify search effectiveness and content gaps over time.

The data for this metric can be retrieved using the `get_no_result_rate()` function  
from [`algolia_connector.py`](../../algolia_connector.py).

## Field Description

| Field            | Description                                                                      |
|------------------|----------------------------------------------------------------------------------|
| `date`           | Day of the event (UTC)                                                           |
| `count`          | Total number of searches executed on this day                                   |
| `noResultCount`  | Number of those searches that returned **zero** results                         |
| `rate`           | Share of searches with no results: `noResultCount / count` (null if `count = 0`) |

> **Note:** The `rate` is computed per day and included in the overall aggregate object as well.

## Schema

```json
{
  "tableName": "algolia_no_result_rate",
  "primaryKey": "date",
  "columns": [
    { "name": "date",           "dataType": "string"  },
    { "name": "noResultCount", "dataType": "integer" },
    { "name": "count",         "dataType": "integer" },
    { "name": "rate",          "dataType": "float"   }
  ]
}
```

> Schema returned by `get_no_result_rate_schema()`, defined in [`algolia_connector.py`](../../algolia_connector.py).

## How to Analyze

| Insight                          | Metric/Field                | Description                                                              |
|----------------------------------|-----------------------------|--------------------------------------------------------------------------|
| Daily failure rate               | `rate`                      | Percentage of searches that returned no results per day                  |
| Peak problem days                | `rate`, `noResultCount`     | Identify days with exceptionally high search failure                     |
| Trend tracking                   | `rate` over time            | Monitor improvements or regressions in search coverage                   |
| Search traffic context           | `count`                     | Understand if high failure occurred on low or high volume days           |
| Overall performance              | Aggregated `rate`           | Total no result count / total search count for entire period             |

## Joins

`No Result Rate` can be joined with other **date-based metrics** using the `date` field:

| Related Metric           | Join Key | Available Fields             | Purpose                                                                 |
|--------------------------|----------|-------------------------------|-------------------------------------------------------------------------|
| `Search Count`           | `date`   | `count`                       | Compare total search traffic vs. failure rate                           |
| `Click Through Rate`     | `date`   | `clickCount`, `rate`          | Understand if low results correlate with poor engagement                |
| `Users Count`            | `date`   | `count`                       | See if failed searches affect active user behavior                      |

> This table **can nott** be joined with metrics like `Top Searches` or `Searches No Results`, which do not contain a `date` field.