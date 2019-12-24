# dataPhD_Rx09-11_repo01

**_Geolocated sample information for rock specimens collected between 2009 and 2011 in west-central Yukon - Data repository 1_**

* * *

This data repository contains a subset of geolocated geoscientific observations collected between 2009 and 2011 by [Witold Ciolkiewicz](https://www.linkedin.com/in/witold-c/) in west-central [Yukon](https://www.google.com/maps/place/Yukon/).  The data describes the location and selected attributes of a set of rock samples currently (December 2019) in storage at the Department of Earth, Ocean and Atmospheric Sciences ([EOAS](https://www.eoas.ubc.ca)) of the University of British Columbia ([UBC](https://www.ubc.ca)).  

The dataset was produced following a request for information received from Jim Ryan of the Geological Survey of Canada ([GSC](https://www.nrcan.gc.ca/science-data/research-centres-labs/geological-survey-canada)).

The observations were collected during field research that was carried out as part of Ph.D. studies conducted by Witold Ciolkiewicz at the UBC Mineral Deposit Research Unit ([MDRU](https://www.mdru.ubc.ca)) under the supervision of [James Mortensen](https://www.eoas.ubc.ca/people/jamesmortensen) (MDRU-UBC) and [Craig Hart](https://www.linkedin.com/in/craig-hart-a2132419) (MDRU-UBC), with external supervision by Jim Ryan (GSC).

The Ph.D. research was supported by the Geological Survey of Canada ([GSC](https://www.nrcan.gc.ca/science-data/research-centres-labs/geological-survey-canada)), the Yukon Geological Survey ([YGS](https://yukon.ca/en/science-and-natural-resources/geology)) and the Natural Sciences and Engineering Research Council of Canada ([NSERC](https://www.nserc-crsng.gc.ca)), through a grant to the [Yukon Gold Project](http://old.mdru.ubc.ca/home/research/yg/yg.php).

# License

This project and its associated output dataset (file _CiolkiewiczW_dataPhD_Rx09-11_repo01.csv_) are licensed under the terms of the Creative Commons Attribution Non Commercial No Derivatives 4.0 International (CC-BY-NC-ND-4.0; see _LICENSE.md_).

# Recommended citation

Ciolkiewicz, W. (2019), dataPhD_Rx09-11_repo01: Geolocated sample information for rock specimens collected between 2009 and 2011 in west-central Yukon - Data repository 1, online: <https://github.com/deepVector/dataPhD_Rx09-11_repo01>

# Source data

## Witold_samples_no_info.xlsx

The file _Witold_samples_no_info.xlsx_ was received from Jim Ryan (GSC) on 13NOV2019.  

The file:

(1) contains a list of rock sample numbers (_n_=170) from the Ph.D. research of Witold Ciolkiewicz that is of interest to the Geological Survey of Canada, and

(2) specifies the scope of the requested information, as follows:

| Sample ID | Source | Sampler | Zone | Latitude | Longitude | Datum | UTM Easting | UTM Northing | Elevation | Loc_Desc\* |
| --------- | ------ | ------- | ---- | -------- | --------- | ----- | ----------- | ------------ | --------- | ---------- |

\* It is assumed that _Loc_Desc_ refers to a description of the collected rock sample.

## Rock sample information from 2009-2011 field research in west-central Yukon

Rock sample locations and field lithological observations were accessed from proprietary project datasets that were produced with the _Ganfeld_ digital field data collection framework developed by [Shimamura, Williams and Buller (2008)](https://doi.org/10.4095/226214) for the Geological Survey of Canada:

| Database             | Type                                                           | Dataset          | Dataset description                                                                                                                                                               |
| -------------------- | -------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vData_field_CONF.gdb | [ArcGIS 10.2](https://resources.arcgis.com/en/help/main/10.2/) | STATION_wc_LIVE  | Includes a description of the geographic location, date, general site information, and observation type ([Shimamura, Williams and Buller, 2008](https://doi.org/10.4095/226214)). |
| vData_field_CONF.gdb | [ArcGIS 10.2](https://resources.arcgis.com/en/help/main/10.2/) | EARTHMAT_wc_LIVE | Description of the rocks at the station location ([Shimamura, Williams and Buller, 2008](https://doi.org/10.4095/226214)).                                                        |
| vData_field_CONF.gdb | [ArcGIS 10.2](https://resources.arcgis.com/en/help/main/10.2/) | SAMPLE_wc_LIVE   | Sample details, including sample type (e.g. _hand specimen_) and purpose (e.g. _representative lithology_).                                                                       |

# Data preparation

## Format conversion

| Old dataset                 | New dataset                       | Utility                                                     |
| --------------------------- | --------------------------------- | ----------------------------------------------------------- |
| Witold_samples_no_info.xlsx | Witold_samples_no_info.csv        | [LibreOffice](https://www.libreoffice.org/) Calc v. 6.3.3.2 |
| STATION_wc_LIVE             | STATION_wc_LIVE_10wci_Select.csv  | [QGIS Desktop](https://qgis.org) v. 3.10.1                  |
| EARTHMAT_wc_LIVE            | EARTHMAT_wc_LIVE_10wci_Select.csv | [QGIS Desktop](https://qgis.org) v. 3.10.1                  |
| SAMPLE_wc_LIVE              | SAMPLE_wc_LIVE_10wci_Select.csv   | [QGIS Desktop](https://qgis.org) v. 3.10.1                  |

## Data pre-processing

### Witold_samples_no_info.csv

1.  Sample identifiers were reviewed, errors were manually cleaned.

    1.1.  Example: An incorrect sample identifier as provided (_09WC**1**_):

        09WC1053A1

    Corrected sample number (to _09WC**I**_):

        09WCI053A1

2.  Duplicate sample IDs (47%) were removed.

    2.1. Script: _data_prep.py_

3.  Fixed sample numbering errors in the request file.

    3.1.  Example:

    Sample number as provided (missing part of the suffix):

        09WCI043A1

    Corrected sample number:

        09WCI043A01

## Data fusion

Sample numbers from _Witold_samples_no_info.csv_ were matched with the corresponding information from the datasets _EARTHMAT_wc_LIVE_, _SAMPLE_wc_LIVE_, and _STATION_wc_LIVE_.  The selected entries from all three geospatial layers were merged into a single dataset.

1.  Script: _data_merge.py_

# Output data

The output dataset _CiolkiewiczW_2019_dataPhD_Rx09-11_repo01.csv_ provides descriptions and location data for a suite of rock samples from the Ph.D. research of Witold Ciolkiewicz that is of interest to the Geological Survey of Canada.

The included data items (e.g. _LITHGROUP_, _LITHDETAIL_) were selected to provide a detailed description of the collected rock samples.  

## Dataset summary

| Attribute  | Source dataset   | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| STATIONID  | STATION_wc_LIVE  | This is a unique key (e.g. _10WCI010_) that identifies each station stop based on year (e.g. 2010 = 10), the geologist's ID (e.g. _WCI_ for "Witold Ciolkiewicz" or _RAYWC_, for "Witold Ciolkiewicz as a member of the GSC field team supervised by Jim Ryan"), and an incrementing number up to 999 stations for one field year (modified after [Shimamura, Williams and Buller, 2008](https://doi.org/10.4095/226214)). |
| EARTHMATID | EARTHMAT_wc_LIVE | The _EARTHMATID_ (e.g. _10WCI010A_) is a unique ID for the rock being described, created by appending a letter of the alphabet to the StationID.  The dominant rock type is usually denoted with the letter _A_, followed by _B_ for a second, less abundant rock type (e.g. a minor intrusion), etc. (modified after [Shimamura, Williams and Buller, 2008](https://doi.org/10.4095/226214)).                             |
| SAMPLEID   | SAMPLE_wc_LIVE   | This is a unique ID for the collected rock sample (e.g. _10WCI010A01_) created by appending a two-digit numerical code to the EARTHMATID (adapted from [Shimamura, Williams and Buller, 2008](https://doi.org/10.4095/226214)).  The code _01_ usually denotes a reference sample, _02_ a sample intended for lithogeochemical analysis, and _03_ a sample that will be used for a geochronological study.                 |
| Source     |                  | Sample provenance / source project.                                                                                                                                                                                                                                                                                                                                                                                        |
| Sampler    |                  | Name of the field mapper / sampler.                                                                                                                                                                                                                                                                                                                                                                                        |
| ELEVATION  | STATION_wc_LIVE  | Elevation, as recorded by the GPS.  Units: metres above the mean sea level.                                                                                                                                                                                                                                                                                                                                                |
| X_WGS84    | STATION_wc_LIVE  | Longitude.  Cartographic Reference System: World Geodetic System 1984 (WGS84).                                                                                                                                                                                                                                                                                                                                             |
| Y_WGS84    | STATION_wc_LIVE  | Latitude.  Cartographic Reference System: World Geodetic System 1984 (WGS84).                                                                                                                                                                                                                                                                                                                                              |
| SLSNOTES   | STATION_wc_LIVE  | Notes describing the mapping station.                                                                                                                                                                                                                                                                                                                                                                                      |
| SAMPLETYPE | SAMPLE_wc_LIVE   | Type of the collected sample, e.g. _hand_, _core_.                                                                                                                                                                                                                                                                                                                                                                         |
| PURPOSE    | SAMPLE_wc_LIVE   | Purpose of sampling, e.g. _geochemistry_, _geochronology_.                                                                                                                                                                                                                                                                                                                                                                 |
| NOTES      | SAMPLE_wc_LIVE   | Notes associated with the sample, e.g. _by a claim marker marked "OJ"_.                                                                                                                                                                                                                                                                                                                                                    |
| LITHGROUP  | EARTHMAT_wc_LIVE | General rock group, e.g. _plutonic_, _volcanic_.                                                                                                                                                                                                                                                                                                                                                                           |
| LITHTYPE   | EARTHMAT_wc_LIVE | Type of the observed rock, e.g. _felsic_, _mafic_.                                                                                                                                                                                                                                                                                                                                                                         |
| LITHDETAIL | EARTHMAT_wc_LIVE | Detailed rock ID, e.g. _granodiorite_.                                                                                                                                                                                                                                                                                                                                                                                     |
| MODTEXTURE | EARTHMAT_wc_LIVE | Description of the observed rock texture, e.g. _porphyritic_.                                                                                                                                                                                                                                                                                                                                                              |
| GRCRYSIZE  | EARTHMAT_wc_LIVE | Average grain size of the rock-forming minerals, e.g. _fine grained &lt;1 mm_.                                                                                                                                                                                                                                                                                                                                             |
| MAGSUSCEPT | EARTHMAT_wc_LIVE | See section _Magnetic susceptibility measurements_.                                                                                                                                                                                                                                                                                                                                                                        |

\* _Note_: For a detailed description of the attributes listed in capital letters, please see the [Geological Survey of Canada Open File 5912](https://doi.org/10.4095/226214).

## Cartographic Reference System

The location data is provided in the World Geodetic System 1984 (WGS84) Cartographic Reference System, as implemented by [ArcGIS 10.2](https://resources.arcgis.com/en/help/main/10.2/).

## Magnetic susceptibility measurements (MAGSUSCEPT)

Field magnetic susceptibility measurements (MAGSUSCEPT) were performed with a high-precision (sensitivity 1\*10<sup>-6</sup> SI units, range 0.000 ― 999\*10<sup>-3</sup> SI units) handheld Magnetic Susceptibility Meter SM-20 ([GF Instruments, 2019](http://www.gfinstruments.cz/index.php?menu=gi&smenu=ims&cont=sm_&ear=ov)). The instrument uses a sensor with diameter of 50 mm that collects 90% of measuring signal from the first 20 mm of the rock.

At each mapping station, the magnetic susceptibility of each investigated lithology was measured multiple times (usually 5 to 10). The measured data were interpreted on the spot, and the value considered most representative of the lithological unit was recorded as the MAGSUSCEPT.                                                                                                                                                                                                          

# Bibliography

Shimamura, K., Williams, S.P., Buller, G., 2008, _GanFeld user guide: a map-based field data capture system for geologists_, Geological Survey of Canada, Open File 5912, 2008, 90 pages; 1 CD-ROM, <https://doi.org/10.4095/226214> (Open Access).

GF Instruments, s.r.o., 2019, _SM-20 - Magnetic Susceptibility Meter_, online: <http://www.gfinstruments.cz/index.php?menu=gi&smenu=ims&cont=sm_&ear=ov>, accessed 20 December 2019.
