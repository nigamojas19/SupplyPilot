import pandas as pd

df = pd.read_csv("fact_aggregate.csv")
df["order_placement_date"] = pd.to_datetime(
    df["order_placement_date"], format="%d-%m-%Y"
).dt.strftime("%Y-%m-%d")
df.to_csv("fact_aggregate_fixed.csv", index=False)