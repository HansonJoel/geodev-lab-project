import geopandas as gpd

lga = gpd.read_file("data/Processed/wards_uyo_clipped.gpkg", layer="wards_uyo_clipped")

print(lga.head())
print("Rows and Columns: ", lga.shape)
print(lga.geom_type.value_counts())
print("CRS: ",lga.crs)


