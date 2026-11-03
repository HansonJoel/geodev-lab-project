## CRS and Data Preparation

### Data Sources
The following datasets were downloaded and prepared for the project:

- **Health Facilities:** GRID3 / Akwa Ibom PHCDA
- **LGA Boundaries:** GRID3
- **Population Data:** WorldPop
- **Road Network:** OpenStreetMap (OSM)

### Data Processing
- All datasets were clipped to the study area (Uyo LGA).
- All vector layers were reprojected to **EPSG:26332 – Minna / UTM Zone 32N**.

### Data Management
- Processed working files are stored in `data/processed/`.
- Original downloaded datasets are preserved in `data/raw/` and remain untouched.
