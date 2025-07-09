# Project Usage

This guide shows how to use the Algolia Analytics Connector after setup and how to explore, extend, or build your own metrics.

## Documentation Overview

Once the server is running (`python algolia_connector.py`), open:

**http://localhost:8000**

You'll see categorized metric links and schema endpoints.  
For a full overview of all available routes, see:  
[`docs/metric-endpoints.md`](./metric-endpoints.md)

## Exploring with Polars

The script [`polars_test.py`](../polars_test.py) lets you load, clean, and analyze the data using Polars.

Example use cases:

- Top search terms
- Click position analysis
- No-result rate breakdown
- CTR calculation

## Adding Your Own Metrics

To add your own metrics:

1. Define a new function in `algolia_connector.py`
2. Add a corresponding schema function 
3. Register the endpoint in the `ENDPOINTS` list
4. Update the `Handler.do_GET()` to handle your new path

Your new metric will now appear in the index UI and respond to HTTP requests.