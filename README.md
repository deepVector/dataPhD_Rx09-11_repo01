# dataPhD_Rx09-11_repo01

**_Geolocated sample information for rock specimens collected between 2009 and 2011 in west-central Yukon - Data repository 1_**

* * *

This data repository contains a subset of geolocated geoscientific observations collected between 2009 and 2011 by [Witold Ciolkiewicz](https://www.linkedin.com/in/witold-c/) in west-central [Yukon](https://www.google.com/maps/place/Yukon/).  The data describes the location and selected attributes of a set of rock samples currently (December 2019) in storage at the Department of Earth, Ocean and Atmospheric Sciences ([EOAS](https://www.eoas.ubc.ca)) of the University of British Columbia ([UBC](https://www.ubc.ca)).  The dataset was produced following a request for information received from Jim Ryan of the Geological Survey of Canada ([GSC](https://www.nrcan.gc.ca/science-data/research-centres-labs/geological-survey-canada)).

The observations were collected during field research that was carried out as part of Ph.D. studies conducted by Witold Ciolkiewicz at the UBC Mineral Deposit Research Unit ([MDRU](https://www.mdru.ubc.ca)) under the supervision of [James Mortensen](https://www.eoas.ubc.ca/people/jamesmortensen) (MDRU-UBC) and [Craig Hart](https://www.linkedin.com/in/craig-hart-a2132419) (MDRU-UBC), with external supervision by Jim Ryan (GSC).

The Ph.D. research was supported by the Geological Survey of Canada ([GSC](https://www.nrcan.gc.ca/science-data/research-centres-labs/geological-survey-canada)), the Yukon Geological Survey ([YGS](https://yukon.ca/en/science-and-natural-resources/geology)) and the Natural Sciences and Engineering Research Council of Canada ([NSERC](https://www.nserc-crsng.gc.ca)), through a grant to the [Yukon Gold Project](http://old.mdru.ubc.ca/home/research/yg/yg.php).

# License

This project and its associated output dataset (file _CiolkiewiczW_dataPhD_Rx09-11_repo01.csv_) are licensed under the terms of the Creative Commons Attribution Non Commercial No Derivatives 4.0 International (CC-BY-NC-ND-4.0; see _LICENSE.md_).

# Recommended citation

Ciolkiewicz, W. (2019), dataPhD_Rx09-11_repo01: Geolocated sample information for rock specimens collected between 2009 and 2011 in west-central Yukon - Data repository 1, online: <https://github.com/deepVector/dataPhD_Rx09-11_repo01>

# Source data

## Witold_samples_no_info.xlsx

The file _Witold_samples_no_info.xlsx_ was received from Jim Ryan (GSC) on 13NOV2019.  The file defines the subset of rock sample numbers from the Ph.D. research of Witold Ciolkiewicz of interest to the GSC and the scope of the requested information, including:

| Sample ID | Source | Sampler | Zone | Latitude | Longitude | Datum | UTM Easting | UTM Northing | Elevation | Loc_Desc |
| --------- | ------ | ------- | ---- | -------- | --------- | ----- | ----------- | ------------ | --------- | -------- |

## Rock sample information from 2009-2011 field research in west-central Yukon

Rock sample locations and field lithological observations were accessed from a proprietary internal database.

| Database             | Type                                                           | Dataset        | Coordinate Reference System |
| -------------------- | -------------------------------------------------------------- | -------------- | --------------------------- |
| vData_field_CONF.gdb | [ArcGIS 10.2](https://resources.arcgis.com/en/help/main/10.2/) | SAMPLE_wc_LIVE | NAD83 / Yukon Albers        |

# Data processing

## Format conversion

| Old dataset                         | New dataset                             | Type                                                   |
| ----------------------------------- | --------------------------------------- | ------------------------------------------------------ |
| Witold_samples_no_info.xlsx         | ../dtWorking/Witold_samples_no_info.csv | Comma-separated values                                 |
| vData_field_CONF.gdb/SAMPLE_wc_LIVE | ../dtWorking/SAMPLE_wc_LIVE.gpkg        | [GeoPackage](https://en.wikipedia.org/wiki/GeoPackage) |

## Coordinate Reference Systems (CRS) conversion

| Dataset        | New CRS                                                                                                                                 | Conversion utility                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| SAMPLE_wc_LIVE | [EPSG:4326 - WGS 84 - Geographic](https://docs.qgis.org/3.4/en/docs/user_manual/working_with_projections/working_with_projections.html) | [QGIS](https://qgis.org/) v.3.10.1 |

CRS definition: EPSG:4326 - WGS 84 - Geographic (source: QGIS v.3.10.1)

    WGS 84
    WKT
    GEODCRS["WGS 84",
        DATUM["World Geodetic System 1984",
            ELLIPSOID["WGS 84",6378137,298.257223563,
                LENGTHUNIT["metre",1]]],
        PRIMEM["Greenwich",0,
            ANGLEUNIT["degree",0.0174532925199433]],
        CS[ellipsoidal,2],
            AXIS["geodetic latitude (Lat)",north,
                ORDER[1],
                ANGLEUNIT["degree",0.0174532925199433]],
            AXIS["geodetic longitude (Lon)",east,
                ORDER[2],
                ANGLEUNIT["degree",0.0174532925199433]],
        AREA["World"],
        BBOX[-90,-180,90,180],
        ID["EPSG",4326]]
    Proj4
    +proj=longlat +datum=WGS84 +no_defs
    Extent
    -180.00, -90.00, 180.00, 90.00

## Data cleaning

1.  Sample numbers in the file _Witold_samples_no_info.csv_ were reviewed, errors were manually cleaned.

    1.1.  E.g. from an incorrect sample number _09WC**1**053A1_ to the correct _09WC**I**053A1_.
