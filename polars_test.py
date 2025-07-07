import json, polars as pl
from algolia_connector import  *

# Polars data-type mapping (Python -> Polars)
TYPE_MAP = {
    "string":  pl.String,
    "integer": pl.Int64,
    "float":   pl.Float64,
    "boolean": pl.Boolean,
    "date":    pl.Date,
    "json":         pl.String,       
    "list<int>":    pl.List(pl.Int64),
    "list<float>":  pl.List(pl.Float64),
    "list<string>": pl.List(pl.String),
    "list<mixed>":  pl.List   
}

# Converts data from list or dict values to JSON string for Polars compatibility
def clean_rows(rows: list[dict]) -> list[dict]:
     return [
        {
            key: (json.dumps(value) if isinstance(value, dict) else value)
            for key, value in row.items()
        }
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
    # Top search
print("\nTop Search:", df_top_searches.sort("count", descending=True)[0, :])

# Searches count
searches_count_rows = get_searches_count()["dates"]
serches_count_schema = get_searches_count_schema()['columns']
df_searches_count = build_df(searches_count_rows, serches_count_schema)
print("\nSearches Count: ")
print(df_searches_count)
    # Max search count
print("\nHighest Search Count in a day:", df_searches_count["count"].max())
print("\nTotal Searches:", df_searches_count["count"].sum())

# Searches no result
searches_no_results_rows = get_searches_no_results()["searches"]
searches_no_results_schema = get_searches_no_results_schema()["columns"]
df_searches_no_results = build_df(searches_no_results_rows, searches_no_results_schema)
print("\nSearches no results: ")
print(df_searches_no_results)
    # Top 10 searches result
print("\nTop 10 searches no result: ", df_searches_no_results.sort("count", descending=True).head(10))

# No result rate
no_result_rate_rows = get_no_result_rate()["dates"]
no_result_rate_schema = get_no_result_rate_schema()["columns"]
df_no_result_rate = build_df(no_result_rate_rows, no_result_rate_schema)
df_no_result_rate = df_no_result_rate.filter(pl.col("count")>0) # Days with min. 1 search
df_no_result_rate = df_no_result_rate.with_columns((pl.col("rate")*100).round(2).alias("rate_percentage"))
print("\nNo result rate: ")
print(df_no_result_rate.select(["date", "noResultCount", "count", "rate_percentage"]))
     # no result rate overall number
total_searches = df_searches_count["count"].sum()
total_no_results = df_no_result_rate["noResultCount"].sum()
overall_nrr = round(total_no_results / total_searches * 100, 2)
print(f"\nNo-Result-Rate: {overall_nrr}%")
    # Days with >10% No-Result-Rate
threshold = 0.10
print("\n>10% No-Result-Rate: ", df_no_result_rate.filter(pl.col("rate") > threshold).sort("rate", descending = True))

# Top hits
top_hits_rows = get_top_hits()["hits"]
top_hits_schema = get_top_hits_schema()["columns"]
df_top_hits = build_df(top_hits_rows, top_hits_schema)
print("\nTop hits: ")
print(df_top_hits)

# Searches no clicks
searches_no_clicks_rows = get_searches_no_clicks()["searches"]
searches_no_clicks_schema = get_searches_no_clicks_schema()["columns"]
df_searches_no_clicks = build_df(searches_no_clicks_rows, searches_no_clicks_schema)
print("\nSearches no clicks: ")
print(df_searches_no_clicks)
    # no clicks rate
total_no_clicks = df_searches_no_clicks["count"].sum()
total_searches  = df_searches_count["count"].sum()
no_click_rate   = round(total_no_clicks / total_searches * 100, 2)
print(f"No-Clicks-Rate: {no_click_rate}%")     

# Click position
click_positions_rows = get_click_positions()["positions"]
click_positions_schema = get_click_positions_schema()["columns"]
df_click_positions = build_df(click_positions_rows, click_positions_schema)
print("\nClick positions: ")
print(df_click_positions)
    # Average click positions (convert from json string to list)
df = (
    df_click_positions
    .with_columns([
        pl.col("position").list.get(0).alias("pos_start"),
        pl.col("position").list.get(1).alias("pos_end"),
        ((pl.col("position").list.get(0) + pl.col("position").list.get(1)) / 2).alias("pos_mean")
    ])
)
df_nonzero = df.filter(pl.col("clickCount") > 0)    # just positions that were clicked
average_position = ((df_nonzero["pos_mean"] * df_nonzero["clickCount"]).sum()/ df_nonzero["clickCount"].sum())
print("\nAverage click position: ", average_position)
    # Percentage of all clicks position
total = df_nonzero["clickCount"].sum()
print("\nPercentage of click position: ", df_nonzero.with_columns((pl.col("clickCount")/total*100).alias("percentage")).select(["clickCount", "pos_mean", "percentage"])) 
    # Click Through rate
clicks_total = df_click_positions["clickCount"].sum()
searches_total = df_searches_count["count"].sum()
ctr = clicks_total / searches_total
print(f"\nClick-through-rate: {ctr*100:.2f}%") 

# Click through rate table
click_through_rate_rows = get_click_through_rate()["dates"]
click_through_rate_schema = get_click_through_rate_schema()["columns"]
df_ctr = build_df(click_through_rate_rows, click_through_rate_schema)
print("\nGet click through rate table :", df_ctr)

# Users count
users_count_rows = get_users_count()["dates"]
users_count_schema = get_users_count_schema()["columns"]
df_users_count = build_df(users_count_rows, users_count_schema)
print("\nNumber of Users: ")
print(df_users_count)
    # Sum of users
print("\nTotal Users: ", df_users_count["count"].sum())
    # Rolling mean last 7 days of user count
print("\nMoving average last 7 days of user count: ", df_users_count.with_columns(pl.col("count").rolling_mean(window_size=7).alias("moving_average")))

# Top countries
top_countries_rows = get_top_countries()["countries"]
top_countries_schema = get_top_countries_schema()["columns"]
df_top_countries = build_df(top_countries_rows, top_countries_schema)
print("\nTop countries: ", df_top_countries)
    # Percentage per country
total = df_top_countries["count"].sum()
print("\nPercentage per Country: ", df_top_countries
      .with_columns((pl.col("count")/total*100).round(2).alias("country_pecentage"))
      .sort("country_pecentage", descending = True))

# Top filter attribtues
top_filter_attributes_rows = get_top_filter_for_attributes()["attributes"]
top_filter_attributes_schema = get_top_filter_for_attributes_schema()["columns"]
df_top_filter_attributes = build_df(top_filter_attributes_rows, top_filter_attributes_schema)
print("\nTop filter attributes: ", df_top_filter_attributes.sort("count", descending= True))
    # Percentage per filter attribute
print("Percentage of Top filter Attributes: ")
print(df_top_filter_attributes.with_columns(((pl.col("count")/pl.col("count").sum())*100).round(2).alias("percentage")))

