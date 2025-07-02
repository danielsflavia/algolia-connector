import json, polars as pl
from algolia_connector import get_top_searches, get_top_searches_schema

rows = get_top_searches()["searches"]

rows = [
    {key: (json.dumps(value) if isinstance(value, (list, dict)) else value) for key, value in row.items()}  # falls liste oder dict wandelt um in json string
    for row in rows
]

# Schema-Mapping to polars data types 
type_map = {"string": pl.String, "integer": pl.Int64,
            "float": pl.Float64, "boolean": pl.Boolean, "date": pl.Date}

# erstellt Schema geht alle c Spalten durch
schema = {c["name"]: type_map.get(c["dataType"], pl.String) 
          for c in get_top_searches_schema()["columns"]}

# Dataframe
print(pl.from_dicts(rows, schema=schema))

