import pandas as pd

df = pd.read_csv("output.csv")

averaged_df = df.groupby("Country").mean().reset_index()

averaged_df.to_csv("averaged_output.csv", index=False)

print(averaged_df)
