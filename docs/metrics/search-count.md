# Search Count

## Description

Returns the total number of searches performed per day.  
This metric is useful for tracking search volume trends over time, measuring user engagement, and monitoring the impact of product changes or marketing campaigns.

## Field Description

| Field     | Description                                 |
|-----------|---------------------------------------------|
| `date`    | The calendar date in `YYYY-MM-DD` format     |
| `count`   | Total number of searches performed on that date |


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

## How to Analyze

You can use the `Search Count` metric to:

- **Plot search trends** over time (daily, weekly, rolling average)
- **Identify spikes or drops** in usage
- **Normalize other metrics** (e.g. clicks or conversions per 1,000 searches)
- **Detect seasonal patterns** and correlate with campaigns, features, or events


## Related Metrics & Joins

| Related Metric                          | Join Key | Purpose                                        |
|----------------------------------------|----------|------------------------------------------------|
| [Click Through Rate](./click-through-rate.md) | `date`   | Compare search volume with engagement levels   |
| [No Results](./no-results.md)                | `date`   | Monitor how many searches return zero results |
| [User Count](./user-count.md)                | `date`   | Compare number of searches per active user    |
