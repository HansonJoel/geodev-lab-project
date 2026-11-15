import pandas as pd

pop = pd.read_csv("data/Raw/Akwa_Ibom_LGA_and_Population.csv")

big = pop[pop["population"] > 100000]
print(big)
print(f"There are {len(big)} LGA with population greater than 100,000")

ranked = pop.sort_values("population", ascending=False)
print(ranked.head(3))

