# Top Hits

## Description

Returns the most clicked individual results across all tracked searches.  
Each hit represents a clicked search result, including its unique identifier and click count.

> **Note:**  
> The `hit` value typically includes a document ID and a full URL or identifier string.  
> The click count reflects how many times that result was clicked across all searches.

## Field Description

| Field     | Description                                                |
|-----------|------------------------------------------------------------|
| `hit`     | Identifier of the clicked result (often contains the URL)  |
| `count`   | Total number of times this result was clicked              |

## Schema

```json
{
  "tableName": "algolia_top_hits",
  "primaryKey": "hit",
  "columns": [
    { "name": "hit",   "dataType": "string" },
    { "name": "count", "dataType": "integer" }
  ]
}
```

## How to Analyze

| Insight                      | Field      | Description                                                   |
|-----------------------------|------------|---------------------------------------------------------------|
| Most clicked documents      | `hit`      | Identify the most frequently clicked content or resources     |
| Result popularity ranking   | `count`    | Sort by click count to evaluate what users engage with most   |
| Click concentration         | —          | Assess whether a small number of hits dominate user clicks    |

> You can use this metric to understand content engagement and popularity at the document or URL level.


## Joins

`Top Hits` is **not directly joinable** with other metrics.

- The `hit` field is a composite identifier (usually prefixed with an ID and followed by a URL), and doesn't match any search-level or date-level keys.
- You can still analyze this metric **independently**, or map part of the URL to content metadata (e.g., page category or section) externally.
