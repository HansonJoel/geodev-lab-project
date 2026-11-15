import geopandas as gpd

lga = gpd.read_file("data/Processed/wards_uyo_clipped.gpkg", layer="wards_uyo_clipped")

first = lga.iloc[0]
print(first)    

print("valid: ", first.geometry.is_valid)
print("Centriod: ", first.geometry.centroid)