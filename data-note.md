Week 2 Data Note — Estate Geospatial Operations & Incident Management Platform
Project Area
Ewet Housing Estate, Uyo LGA, Akwa Ibom State, Nigeria

The project data was obtained from Overture Maps and opened/inspected in QGIS.

Datasets
1. Roads
Source: Overture Maps
Geometry: LineString
Features: 574 road segments
Key column: class — describes the road type, such as residential, tertiary, secondary, primary, and unclassified.
Other data: The dataset contains several additional road-related attributes.
Data quality: Several fields contain NULL/missing values.

2. Road Connectors
Source: Overture Maps
Geometry: Point
Features: 373 connector points
Purpose: Represents connection points at road intersections and helps describe the road network.

3. Buildings
Source: Overture Maps
Geometry: Polygon
Features: 8,127 building footprints
Key data: Building geometry and related building attributes.
Data quality: Some attributes contain NULL/missing values.


4. Estate Boundary
Source: OpenStreetMap (OSM), interpreted and digitized in QGIS
Geometry: Polygon
Features: 1 estate boundary
Purpose: Defines the project study area for Ewet Housing Estate.
Data Gaps and Future Data

The currently downloaded datasets provide the basic spatial context for the project. Other datasets will be added as the project develops.
Some operational datasets, such as incident reports, estate assets, incident media, residents, workers, work orders, and maintenance history, will be simulated for testing and development purposes. Where suitable real-world data is available, additional datasets will be incorporated into the project.

Sources:

Overture Maps: https://overturemaps.org/
OpenStreetMap: https://www.openstreetmap.org/
