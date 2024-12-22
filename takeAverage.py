import os
import pandas as pd

df = pd.read_csv("output.csv")

averaged_df = df.groupby("Country").mean().reset_index()

file_exists = os.path.isfile("averaged_output.csv")

averaged_df.to_csv("averaged_output.csv", mode='a', index=False, header=not file_exists)

print(averaged_df)
