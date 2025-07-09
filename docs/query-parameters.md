# Query Parameter Guide

These parameters can be passed to every endpoint to filter, segment, or paginate the results.

| Parameter | Type | Example | Meaning |
|-----------|------|---------|---------|
| `startDate` | YYYY-MM-DD | `startDate=2025-07-01` | Start of period. |
| `endDate`   | YYYY-MM-DD | `endDate=2025-07-08` | End of period. |
| `limit`     | int ≤ 1000 | `limit=50`           | Max items (default 10). |
| `offset`    | int ≥ 0    | `offset=0`           | Pagination offset. |
| `tags`      | string     | `tags=device:mobile%20phone` | Segment by tag (URL-encode AND/OR). |

> Warning: If no data exists in the selected range, the result may be empty.

## Usage Examples

### 1. In the Browser

**http://localhost:8000/top?limit=20&startDate=2025-07-01&endDate=2025-07-08**


### 2. In Python

```python
client.get_top_searches(
    index=INDEX,
    limit=20,
    start_date="2025-07-01",
    end_date="2025-07-08",
    tags="device:mobile phone"
)
```

>  Full Algolia documentation: `https://www.algolia.com/doc/rest-api/analytics/`
