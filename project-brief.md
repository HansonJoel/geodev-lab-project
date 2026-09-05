# GeoDev Lab — Week 1
## Estate Geospatial Operations & Incident Management Platform

### 1. The Question

**How can geospatial technology help estate managers identify, locate, prioritize, assign, track, and analyze infrastructure issues within an estate?**

### 2. Why It Matters

Estate issues such as flooding, blocked drainage, damaged roads, broken streetlights, and waste accumulation are often reported through informal channels, making them difficult to locate, track, and manage.

This project will use GIS to connect incidents and estate assets to their geographic locations, helping managers improve maintenance, decision-making, and resource allocation.

### 3. Data Needed

- Estate boundaries
- Building footprints
- Road network
- Drainage and waterways
- Land use/land cover
- Points of interest and facilities
- Digital Elevation Model (DEM)
- Satellite imagery
- Estate assets
- Incident reports
- Incident media
- Residents and workers
- Work orders
- Maintenance history

### 4. Data Sources

| Data | Source |
|---|---|
| Buildings, roads, waterways, POIs | OpenStreetMap / Overture Maps |
| Estate boundaries | Open data / Synthetic data |
| DEM | OpenTopography / NASA / USGS |
| Satellite imagery | Sentinel-2 / Copernicus |
| Estate assets & operations | Synthetic data initially |
| Incidents & work orders | Generated through the application |

### 5. What I Will Build

A **GIS-enabled Estate Operations and Incident Management Platform** where users can report estate issues with their location and media. Estate managers will view incidents on an interactive map, prioritize and assign work orders, track resolution, and analyze recurring problems.

The project will progressively incorporate spatial analysis such as **proximity, buffers, spatial joins, overlays, terrain analysis, and incident pattern analysis**.

### Data Strategy

The project will combine **real open geospatial data with synthetic operational data**, allowing development and testing without requiring private estate-management datasets.