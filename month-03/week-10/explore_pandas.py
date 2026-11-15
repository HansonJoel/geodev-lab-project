import pandas as pd

pop = pd.read_csv("data/Raw/Akwa_Ibom_LGA_and_Population.csv")

print(pop.head())
print("shape: ", pop.shape)
print("columns: ", list(pop.columns))
print(pop.dtypes)
print(pop.describe())