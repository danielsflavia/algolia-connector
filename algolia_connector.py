from algoliasearch.analytics.client import AnalyticsClientSync
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
import os, json

# API Daten vom env
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


# Endpoints for index page
ENDPOINTS = [
    ("/top",        "Top Searches"),
    ("/count",      "Search Count"),
    ("/noresults",  "Searches Without Results"),
    ("/norate",     "No-Result Rate"),
    ("/hits",       "Top Hits"),
    ("/noclicks",   "Searches No Clicks")
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
        if route == "":
            self._send_html(self._index()); return
        if route == "/top":
            self._send_json(get_top_searches());  return
        if route == "/count":
            self._send_json(get_searches_count()); return
        if route == "/noresults":
            self._send_json(get_searches_no_results()); return
        if route == "/norate":
            self._send_json(get_no_result_rate()); return
        if route == "/hits":
            self._send_json(get_top_hits()); return
        if route == "/noclicks":
            self._send_json(get_searches_no_clicks()); return
        self.send_error(404, "Endpoint not found")

def main():
    HTTPServer(("localhost", 8000), Handler).serve_forever()

if __name__ == "__main__":
    main()