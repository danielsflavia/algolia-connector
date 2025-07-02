import json, polars as pl
from algolia_connector import get_top_searches, get_top_searches_schema, get_searches_count, get_searches_count_schema, get_users_count, get_users_count_schema, get_top_countries, get_top_countries_schema

# Polars data types mapping (Python -> Polars)
TYPE_MAP = {
    "string":  pl.String,
    "integer": pl.Int64,
    "float":   pl.Float64,
    "boolean": pl.Boolean,
    "date":    pl.Date
}

# Daten bereinigen: falls liste oder dict wird es umgewandelt in json string
def clean_rows(rows: list[dict]) -> list[dict]:
    return [
        {key: (json.dumps(value) if isinstance(value, (list, dict)) else value) for key, value in row.items()}
        for row in rows
    ]

# Schema erstellen
def schema_to_polars(schema_cols: list[dict]) -> dict:
    return {c["name"]: TYPE_MAP.get(c["dataType"], pl.String) for c in schema_cols}

# Tabelle bauen
def build_df(rows, schema_cols):
    return pl.from_dicts(clean_rows(rows), schema=schema_to_polars(schema_cols))



# ---- Datenbindung aus Algolia_connctor ---

# Top Searches
top_searches_rows   = get_top_searches()["searches"]
top_searches_schema = get_top_searches_schema()["columns"]
df_top_searches = build_df(top_searches_rows, top_searches_schema)
print("\nTop Searches: ")
print(df_top_searches)
    # Filtern und analysieren
print("\nTop Search:", df_top_searches.sort("count", descending=True)[0, :])

# Searches count
searches_count_rows = get_searches_count()["dates"]
serches_count_schema = get_searches_count_schema()['columns']
df_searches_count = build_df(searches_count_rows, serches_count_schema)
print("\nSearches Count: ")
print(df_searches_count)
    # Filtern und analysieren
print("\nHighest Search Count in a day:", df_searches_count["count"].max())


# Users count
users_count_rows = get_users_count()["dates"]
users_count_schema = get_users_count_schema()["columns"]
df_users_count = build_df(users_count_rows, users_count_schema)
print("\nNumber of Users: ")
print(df_users_count)
    # Filtern und analysieren
print("\nTotal Users: ", df_users_count["count"].sum())

# Top Countries
top_countries_rows = get_top_countries()["countries"]
top_countries_schema = get_top_countries_schema()["columns"]
df_top_countries = build_df(top_countries_rows, top_countries_schema)
print("\nTop countries: ")
print(df_top_countries)

