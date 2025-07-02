import json, polars as pl
from algolia_connector import get_top_searches, get_top_searches_schema, get_searches_count, get_searches_count_schema

# Poars data types mapping
TYPE_MAP = {
    "string":  pl.String,
    "integer": pl.Int64,
    "float":   pl.Float64,
    "boolean": pl.Boolean,
    "date":    pl.Date
}

# falls liste oder dict wandelt um in json string
def clean_rows(rows: list[dict]) -> list[dict]:
    return [
        {key: (json.dumps(value) if isinstance(value, (list, dict)) else value) for key, value in row.items()}
        for row in rows
    ]

def schema_to_polars(schema_cols: list[dict]) -> dict:
    return {c["name"]: TYPE_MAP.get(c["dataType"], pl.String) for c in schema_cols}

def build_df(rows, schema_cols):
    return pl.from_dicts(clean_rows(rows), schema=schema_to_polars(schema_cols))

# Top Searches from Algolia_connector
top_searches_rows   = get_top_searches()["searches"]
top_searches_schema = get_top_searches_schema()["columns"]
df_top_searches = build_df(top_searches_rows, top_searches_schema)
print("\nTop Searches: ")
print(df_top_searches)

# Searches count from Algolia_connector
searches_count_rows = get_searches_count()["dates"]
serches_count_schema = get_searches_count_schema()['columns']
df_searches_count = build_df(searches_count_rows, serches_count_schema)
print("\nSearches Count: ")
print(df_searches_count)


# Filter and Analysis with Data
print("\nHäufigste Suchanfrage:", df_top_searches.sort("count", descending=True)[0, :])