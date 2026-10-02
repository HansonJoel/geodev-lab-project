# GeoDev Lab — Week 1
## Healthcare Accessibility & Service Gab analysis for Uyo Local Government Area

### 1. The Question

**How accessible are healthcare facilities to residents of Uyo Local Government Area, Akwa Ibom State, and which areas have limited access to essential healthcare services?**

### 2. Why It Matters

The answer can help health planners, government agencies, and healthcare managers understand where populations have relatively poor geographic access to healthcare and where additional services or planning attention may be needed. It can also help compare accessibility across wards and, later, across all LGAs in Akwa Ibom State. 

For my GIS growth, the project will move me beyond conventional mapping into network analysis, spatial databases, Python automation, web mapping, and building a reusable geospatial application.


### 3. Data Needed

Akwa Ibom State boundary — polygon providing the state context.
Akwa Ibom State LGAs boundary — polygons for Local Government level accessibility analysis.
Akwa Ibom State ward boundary — polygons for ward-level accessibility analysis.
Health facility locations — point locations of hospitals, PHCs, health centres, clinics and other available healthcare facilities.
Population raster — gridded population estimates for estimating the number of people within different accessibility zones.
Road network — roads within and around Uyo LGA, including road classification.
Road/travel-time information — road classes and/or travel-time data used to estimate movement through the network.
Settlement data — settlement locations/extents for additional population and settlement context.
Optional: healthcare service/capacity information — beds, staffing, equipment or specific services, where reliable data is available.

### 4. Data Sources

Data - Source 
Dataset	Source	Link
LGA boundaries	GRID3 – Nigeria Geospatial Data	GRID3 Nigeria Geospatial Data
State boundary	GRID3 – Nigeria Geospatial Data	GRID3 Nigeria Geospatial Data
Ward boundaries	GRID3 – Operational Wards	GRID3 Nigeria Geospatial Data
Health facilities	GRID3 – Nigeria Health Facilities v2.0	GRID3 Nigeria Geospatial Data
Primary healthcare facilities	Akwa Ibom State Primary Health Care Development Agency (AKSPHCDA)	AKSPHCDA Full List of Primary Healthcare Centers
Population	GRID3 / WorldPop	GRID3 Nigeria Geospatial Data
Road network	OpenStreetMap via Geofabrik Nigeria	Geofabrik Nigeria OSM Download
Travel-time data	GRID3 – Travel Time Friction Surface	GRID3 Nigeria Geospatial Data
Settlement extents/names	GRID3 – Nigeria Settlements	GRID3 Nigeria Geospatial Data


### 5. What I Will Build

A **I will build a web-based healthcare accessibility map and dashboard for Uyo LGA that allows a user to view healthcare facilities, population distribution, wards, roads and modelled travel-time accessibility on an interactive map. 
The system will be designed as a reusable workflow so that the same analysis can later be run for any LGA in Akwa Ibom State, allowing users to select an LGA and view its healthcare accessibility and potential service-gap results.**.

