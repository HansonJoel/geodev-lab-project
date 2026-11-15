import pandas as pd
import geopandas as gpd

table =pd.read_csv("data/Raw/")


health_facilities = gpd.GeoDataFrame()