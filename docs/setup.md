# Project Overview & Usage

This page expands on the quickstart from the README.  
After setting up the server, here’s how the project is structured and how to work with it.

## Local Server

Once the server is running, you can:

- Open [`http://localhost:8000`](http://localhost:8000) to see the metric UI
- Click on any route to see JSON output
- Append `/schema` to any route to get the data schema

## Metric Categories

| Category      | Example Endpoints             |
|---------------|-------------------------------|
| Search        | `/top`, `/count`, `/noresults` |
| Clicks        | `/clickposition`, `/noclicks` |
| Users         | `/userscount`, `/countries`   |

See full list in [`docs/metric-endpoints.md`](./metric-endpoints.md)

## Exploring with Polars

The script [`polars_test.py`](../polars_test.py) lets you load, clean, and analyze the data using Polars.

Examples include:

- Top search terms
- Click position analysis
- No-result rate breakdown
- CTR calculation

## Extending the Connector

To add your own metrics:

1. Define a new function in `algolia_connector.py`
2. Add a corresponding schema function 
3. Register the endpoint in the `ENDPOINTS` list
4. Update the `Handler.do_GET()` to handle your new path

This approach keeps logic and UI fully decoupled and easy to maintain.