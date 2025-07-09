# Project Usage

This guide shows how to use the Algolia Analytics Connector after setup and how to explore, extend, or build your own metrics.

## Documentation Overview

Once the server is running (`python algolia_connector.py`), open:

**http://localhost:8000**

You will see categorized metric links and schema endpoints that can be explored directly in the browser.  
These cover a **default selection of endpoints and filters**.

See [`docs/query-parameters.md`](./docs/query-parameters.md) for a list of all available filters (`startDate`, `endDate`, `tags`, etc.).

## Exploring with Polars

While the browser UI gives a quick overview, the script [`polars_test.py`](../polars_test.py) lets you deeply explore and analyze all available metrics.

With it, you can:

- Fetch and combine any of the predefined endpoints
- Join tables (e.g., searches + click-through rate)
- Filter, group, and transform the data
- Create custom KPIs directly in Polars

See [`docs/metric-endpoints.md`](./docs/metric-endpoints.md) to learn which tables are available and which fields you can combine.
