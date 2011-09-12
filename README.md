# Mapnik Examples

The purpose of these examples are to give a brief look at what is possible with the [Mapnik library](http://mapnik.org/).

Written for talk that I am giving for [Philly PUG meeting](http://www.meetup.com/phillypug/) on 13 Sept 2011.

## Overview

### Getting the Shapefile Data

I don't include the raw data in this repository. To pull down the data run:

`rake getdata`

### Running the examples

Once you have installed Mapnik, you can just run the examples in python, such as:

`python name_of_file.py`

This will output `name_of_file.png` in an `images` directory.

## World Borders Example

This is the 'Hello World' of Mapnik, taken from [this Mapnik tutorial](http://trac.mapnik.org/wiki/GettingStarted). The result will be an image displaying the borders of the countries of the world.

 * __To Run__ `python world.py`
 * __Output__ images/world.png
 * __Data Source__ [Mapping Hacks](http://mappinghacks.com/data/).
 * __Data Files__ data/world_borders

## World Population Example

This example uses an xml file to specify styling and layers instead writing python code and is taken from [this Mapnik example](http://trac.mapnik.org/wiki/XMLGettingStarted#Step2).

 * __To Run__ `python world_population.py`
 * __Output__ images/world_population.png
 * __Data Source__ [Mapnik Tutorial site](http://trac.mapnik.org/attachment/wiki/XMLGettingStarted/world_borders.zip)
 * __Data Files__ data/world_borders_pop

## Addresses Example

This example is meant to show how geographic data can be used to tell a story. In every city of this example, the addresses that have numbers 0-100 are colored differently. The purpose of this coloring can show how the city grew and expanded. This started from a [post on the Cartogrammer blog](http://www.cartogrammar.com/blog/paint-by-numbers/).

In regards to Mapnik, this example shows how to change the styling of the map based on attributes of a shapefile. The sample data from this example came from [Census Tiger line data](http://www.census.gov/cgi-bin/geo/shapefiles2010/main). Select "All Lines" and then the state and county that you want.

 * __To Run__ `python address.py`
 * __Output__ images/ boston.png, newyork.png, philly.png, portland.png
 * __Data Source__ [Census Tiger line data](http://www.census.gov/cgi-bin/geo/shapefiles2010/main)
 * __Data Files__ data/ boston, newyork, philly, portland

## Philly Buildings Example

This is a data set I found through [Open Data Philly](http://opendataphilly.org/). _All_ of Phildelphia's buildings is a powerful dataset and I wanted to see what I could find out. To explore the shapefile, you can run 

`ogrinfo -so -al name_of_shapefile.shp`

The `ogrinfo` command comes when you install the GDAL library and allows you to query shapefile data about a shapefile from the command line. The `-al` (all layers) switch lists all features of all layers; this could get very verbose in some cases but in all of these examples, the shapefiles have one layer. The `-so` (summary only) switch will show summary information about the layer's features, such as attribute name and attribute type.

In this case, running the above command on the `PhiladelphiaBuildings200712.shp` file returns the following data:

    Layer name: PhiladelphiaBuildings200712
    Geometry: Polygon
    Feature Count: 390293
    Extent: (2645877.045900, 178938.659570) - (2761445.799878, 343055.989383)
    Layer SRS WKT:
    PROJCS["NAD_1983_StatePlane_Pennsylvania_South_FIPS_3702_Feet",
        GEOGCS["GCS_North_American_1983",
            DATUM["North_American_Datum_1983",
                SPHEROID["GRS_1980",6378137.0,298.257222101]],
            PRIMEM["Greenwich",0.0],
            UNIT["Degree",0.0174532925199433]],
        PROJECTION["Lambert_Conformal_Conic_2SP"],
        PARAMETER["False_Easting",1968500.0],
        PARAMETER["False_Northing",0.0],
        PARAMETER["Central_Meridian",-77.75],
        PARAMETER["Standard_Parallel_1",39.93333333333333],
        PARAMETER["Standard_Parallel_2",40.96666666666667],
        PARAMETER["Latitude_Of_Origin",39.33333333333334],
        UNIT["Foot_US",0.3048006096012192]]
    AREA: Real (19.8)
    PERIMETER: Real (19.8)
    FCODE: Integer (10.0)
    ELEV: Real (19.8)
    SOURCE: String (10.0)
    DATE_UPDAT: String (4.0)
    AREA_1: Real (19.11)
    LEN: Real (19.11)

So, this command outputs a lot of data, but what interests us? If this is the first time that we're seeing this dataset, an important piece of information would the `DATUM` attribute, which specifies the projection of the layer. The other important piece of information this provides are names of all the attributes of the layer. These attributes are what we will use to create an interesting map out of this data.

 * __To Run__ `python philly_buildings.py`
 * __Output__ images/philly_buildings.png
 * __Data Source__ [PASDA](http://www.pasda.psu.edu/uci/PhiladelphiaAgreement.asp?File=http://www.pasda.psu.edu/philacity/data/PhiladelphiaBuildings200712.zip) (via [Open Data Philly](http://opendataphilly.org/opendata/resource/6/buildings/))
 * __Data Files__ data/philly_buildings

## Military Bases Example

 * __To Run__ `python military_bases.py`
 * __Output__ images/military_bases.png
 * __Data Source__ [Military Installations](http://explore.data.gov/National-Security-and-Veterans-Affairs/Military-Installations-Ranges-and-Training-Areas/wcc7-57p3) via Data.gov and [National county borders](http://www.data.gov/geodata/g602085/) via Data.gov
 * __Data Files__ data/military_bases and data/boundaries

## Military Bases Slippy Map Example

 * __To Run__ `liteserv.py military_bases.xml`
 * __Output__ Opening openlayers.html will show the layer produced
 * __Data Source__ DOD Dataset via [Data.gov](http://explore.data.gov/National-Security-and-Veterans-Affairs/Military-Installations-Ranges-and-Training-Areas/wcc7-57p3)
 * __Data Files__ data/military_bases
