from algoliasearch.analytics.client import AnalyticsClientSync
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
import os, json


# API Data from .env
load_dotenv()
APP_ID  = os.getenv("ALGOLIA_APP_ID")
API_KEY = os.getenv("ALGOLIA_ANALYTICS_KEY")
REGION  = os.getenv("ALGOLIA_REGION")
INDEX   = os.getenv("INDEX_NAME")

client = AnalyticsClientSync(APP_ID, API_KEY, REGION)

# Search Metrics connected
def get_top_searches():
    resp = client.get_top_searches(index=INDEX, click_analytics=True)
    return resp.to_dict()

def get_searches_count():
    resp = client.get_searches_count(index=INDEX)
    return resp.to_dict()

def get_searches_no_results():
    resp = client.get_searches_no_results(index=INDEX)
    return resp.to_dict()

def get_no_result_rate():
    resp = client.get_no_results_rate(index=INDEX)
    return resp.to_dict()

def get_top_hits():
    resp = client.get_top_hits(index=INDEX)
    return resp.to_dict()

# Clicks Metrics connected
def  get_searches_no_clicks():
    resp =  client.get_searches_no_clicks(index=INDEX)
    return resp.to_dict()

def get_click_positions():
    resp = client.get_click_positions(index=INDEX)
    return resp.to_dict()

def get_click_through_rate():
    resp = client.get_click_through_rate(index=INDEX)
    return resp.to_dict()

# Users Metrics connected
def get_users_count():
    resp = client.get_users_count(index=INDEX)
    return resp.to_dict()

def get_top_countries():
    resp = client.get_top_countries(index=INDEX)
    return resp.to_dict()

# Top filter for attribute
def get_top_filter_attributes():
    resp = client.get_top_filter_attributes(index=INDEX)
    return resp.to_dict()



# Data Types and Schema function
def _dtype(value):
    if isinstance(value, bool):   return "boolean"
    if isinstance(value, int):    return "integer"
    if isinstance(value, float):  return "float"
    if isinstance(value, str):    return "string" 
    if isinstance(value, (list, tuple)):
        if value and all(isinstance(x, int)   for x in value):
            return "list<int>"
        if value and all(isinstance(x, float) for x in value):
            return "list<float>"
        if value and all(isinstance(x, str)   for x in value):
            return "list<string>"
        return "list<mixed>"                
    if isinstance(value, dict):
        return "json"                     
    return "unknown"

def _guess_primary_key(sample_row):
    for cand in ("id", "objectID", "uid", "uuid", "pk"):
        if cand in sample_row:
            return cand
    return None 

def schema_from_rows(
    rows: list[dict],
    *,
    table_name: str,
    primary_key: str | None = None,
    ):
    if not rows:
        return {
            "tableName": table_name,
            "primaryKey": primary_key,       
            "columns": []
        }

    first = rows[0]
    if primary_key is None:
        primary_key = _guess_primary_key(first)

    return {
        "tableName": table_name,
        "primaryKey": primary_key,           
        "columns": [
            {"name": k, "dataType": _dtype(v)}
            for k, v in first.items()
        ]
    }

    # create schemas for each connector
def get_top_searches_schema():
    return schema_from_rows(
        get_top_searches().get("searches", []),
        table_name="algolia_top_searches",
        primary_key="search"                 
    )

def get_searches_count_schema():
    return schema_from_rows(
        get_searches_count().get("dates", []),
        table_name="algolia_searches_count",
        primary_key="date"
    )

def get_searches_no_results_schema():
    return schema_from_rows(
        get_searches_no_results().get("searches", []),
        table_name="algolia_searches_no_results",
        primary_key="search"
    )

def get_no_result_rate_schema():
    return schema_from_rows(
        get_no_result_rate().get("dates", []),
        table_name="algolia_no_result_rate",
        primary_key="date"
    )

def get_top_hits_schema():
    return schema_from_rows(
        get_top_hits().get("hits", []),
        table_name="algolia_top_hits",
        primary_key="hit"
    )

def get_searches_no_clicks_schema():
    return schema_from_rows(
        get_searches_no_clicks().get("searches", []),
        table_name="algolia_searches_no_clicks",
        primary_key="search"
    )

def get_click_through_rate_schema():
    return schema_from_rows(
        get_click_through_rate().get("dates", []),
        table_name="algolia_click_through_rate",
        primary_key="date"
    )

def get_users_count_schema():
    return schema_from_rows(
        get_users_count().get("dates", []),
        table_name="algolia_users_count",
        primary_key="date"
    )

def get_top_countries_schema():
    return schema_from_rows(
        get_top_countries().get("countries", []),
        table_name="algolia_top_countries",
        primary_key="country"
    )

def get_click_positions_schema():
    return schema_from_rows(
        get_click_positions().get("positions", []),
        table_name="algolia_click_positions",
        primary_key="position"
    )

def get_top_filter_attributes_schema():
    return schema_from_rows(
        get_top_filter_attributes().get("attributes", []),
        table_name="algolia_top_filter_attributes",
        primary_key="attribute"
    )


# Endpoints for index page
ENDPOINTS = [
    ("/top",                      "Top Searches"),
    ("/top/schema",               "Top Searches (Schema)"),
    ("/count",                     "Search Count"),
    ("/count/schema",              "Search Count (Schema)"),
    ("/noresults",                 "No Results"),
    ("/noresults/schema",          "No Results (Schema)"),
    ("/norate",                    "No Result Rate"),
    ("/norate/schema",             "No Result Rate (Schema)"),
    ("/hits",                      "Top Hits"),
    ("/hits/schema",               "Top Hits (Schema)"),
    ("/noclicks",                  "No Clicks"),
    ("/noclicks/schema",           "No Clicks (Schema)"),
    ("/clickposition",             "Click Position"),
    ("/clickposition/schema",      "Click position (Schema)"),
    ("/clickthroughrate",          "Click Through Rate"),
    ("/clickthroughrate/schema",   "Click Through Rate (Schema)"),
    ("/userscount",                "Number of Users"),
    ("/userscount/schema",         "Number of Users (Schema)"),
    ("/countries",                 "Top Countries"),
    ("/countries/schema",          "Top Countries (Schema)"),
    ("/filter",                    "Top Filter Attributes"),
    ("/filter/schema",             "Top Filter Attributes (Schema)")
]


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, obj):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj, indent=2).encode())

    def _send_html(self, html):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())

    # Index page with links
    def _index(self):
        links = "\n".join(
            f'<a class="btn" href="{url}">{label}</a>' for url, label in ENDPOINTS
        )
        return f"""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Algolia Connector</title>
            <style>
                body {{font-family: sans-serif; max-width: 600px; margin: 40px auto;}}
                h1  {{text-align:center}}
                .btn {{
                    display:block; margin:8px 0; padding:10px 14px;
                    border-radius:6px; text-align:center;
                }}
                .btn:hover {{background:#e0e0e0}}
            </style>
        </head>
        <body>
            <h1>Algolia Connector</h1>
            {links}
        </body>
        </html>
        """

    def do_GET(self):
        route = self.path.rstrip("/")
        match route:
            case "":
                self._send_html(self._index())
            case "/top":
                self._send_json(get_top_searches())
            case "/top/schema":
                self._send_json(get_top_searches_schema())
            case "/count":
                self._send_json(get_searches_count())
            case "/count/schema":
                self._send_json(get_searches_count_schema())
            case "/noresults":
                self._send_json(get_searches_no_results())
            case "/noresults/schema":
                self._send_json(get_searches_no_results_schema())
            case "/norate":
                self._send_json(get_no_result_rate())
            case "/norate/schema":
                self._send_json(get_no_result_rate_schema())
            case "/hits":
                self._send_json(get_top_hits())
            case "/hits/schema":
                self._send_json(get_top_hits_schema())
            case "/noclicks":
                self._send_json(get_searches_no_clicks())
            case "/noclicks/schema":
                self._send_json(get_searches_no_clicks_schema())
            case "/clickposition":
                self._send_json(get_click_positions())
            case "/clickposition/schema":
                self._send_json(get_click_positions_schema())
            case "/clickthroughrate":
                self._send_json(get_click_through_rate())
            case "/clickthroughrate/schema":
                self._send_json(get_click_through_rate_schema())
            case "/userscount":
                self._send_json(get_users_count())
            case "/userscount/schema":
                self._send_json(get_users_count_schema())
            case "/countries":
                self._send_json(get_top_countries())
            case "/countries/schema":
                self._send_json(get_top_countries_schema())
            case "/filter":
                self._send_json(get_top_filter_attributes())
            case "/filter/schema":
                self._send_json(get_top_filter_attributes_schema())    
            case _:
                self.send_error(404, "Endpoint not found")

def main():
    server = HTTPServer(("localhost", 8000), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer wurde per Strg+C gestoppt")
    finally:
        server.server_close()   # Port gets free

if __name__ == "__main__":
    main()