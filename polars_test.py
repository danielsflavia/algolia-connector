import json, polars as pl
from algolia_connector import  *

# Polars data-type mapping (Python -> Polars)
TYPE_MAP = {
    "string":  pl.String,
    "integer": pl.Int64,
    "float":   pl.Float64,
    "boolean": pl.Boolean,
    "date":    pl.Date
}

# Converts data from list or dict values to JSON string for Polars compatibility
def clean_rows(rows: list[dict]) -> list[dict]:
    return [
        {key: (json.dumps(value) if isinstance(value, (list, dict)) else value) for key, value in row.items()}
        for row in rows
    ]

# Takes algolia_connector schema and makes it a Polars schema using TYPE_MAP 
def schema_to_polars(schema_cols: list[dict]) -> dict:
    return {c["name"]: TYPE_MAP.get(c["dataType"], pl.String) for c in schema_cols}

# Cleans rows and builds a Polars DataFrame 
def build_df(rows, schema_cols):
    return pl.from_dicts(clean_rows(rows), schema=schema_to_polars(schema_cols))



# ---- Pull data from algolia_connector ---

# Top searches
top_searches_rows   = get_top_searches()["searches"]
top_searches_schema = get_top_searches_schema()["columns"]
df_top_searches = build_df(top_searches_rows, top_searches_schema)
print("\nTop Searches: ")
print(df_top_searches)
    # Filter and analyse
print("\nTop Search:", df_top_searches.sort("count", descending=True)[0, :])

# Searches count
searches_count_rows = get_searches_count()["dates"]
serches_count_schema = get_searches_count_schema()['columns']
df_searches_count = build_df(searches_count_rows, serches_count_schema)
print("\nSearches Count: ")
print(df_searches_count)
    # Filter and analyse
print("\nHighest Search Count in a day:", df_searches_count["count"].max())

# Searches no result
searches_no_results_rows = get_searches_no_results()["searches"]
searches_no_results_schema = get_searches_no_results_schema()["columns"]
df_searches_no_results = build_df(searches_no_results_rows, searches_no_results_schema)
print("\nSearches no results: ")
print(df_searches_no_results)

# No result rate
no_result_rate_rows = get_no_result_rate()["dates"]
no_result_rate_schema = get_no_result_rate_schema()["columns"]
df_no_result_rate = build_df(no_result_rate_rows, no_result_rate_schema)
print("\nNo result rate: ")
print(df_no_result_rate)

# Top hits
###

# Searches no clicks
###

# Users count
users_count_rows = get_users_count()["dates"]
users_count_schema = get_users_count_schema()["columns"]
df_users_count = build_df(users_count_rows, users_count_schema)
print("\nNumber of Users: ")
print(df_users_count)
    # Filter and analyse
print("\nTotal Users: ", df_users_count["count"].sum())

# Top countries
top_countries_rows = get_top_countries()["countries"]
top_countries_schema = get_top_countries_schema()["columns"]
df_top_countries = build_df(top_countries_rows, top_countries_schema)
print("\nTop countries: ")
print(df_top_countries)

