# Mapnik Examples

The purpose of these examples are to give a brief look at what is possible with the [Mapnik library](http://mapnik.org/).

Written for talk that I am giving for [Philly PUG meeting](http://www.meetup.com/phillypug/) on 13 Sept 2011.

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

 * __To Run__ `python philly_buildings.py`
 * __Output__ images/philly_buildings.png
 * __Data Source__ [PASDA](http://www.pasda.psu.edu/uci/PhiladelphiaAgreement.asp?File=http://www.pasda.psu.edu/philacity/data/PhiladelphiaBuildings200712.zip) (via [Open Data Philly](http://opendataphilly.org/opendata/resource/6/buildings/))
 * __Data Files__ data/philly_buildings

## Military Bases Example

 * __To Run__ `python military_bases.py`
 * __Output__ images/military_bases.png
 * __Data Source__ DOD Dataset via [Data.gov](http://explore.data.gov/National-Security-and-Veterans-Affairs/Military-Installations-Ranges-and-Training-Areas/wcc7-57p3)
 * __Data Files__ data/military_bases

## Military Bases Slippy Map Example

 * __To Run__ `liteserv.py military_bases.xml`
 * __Output__ Opening openlayers.html will show the layer produced
 * __Data Source__ DOD Dataset via [Data.gov](http://explore.data.gov/National-Security-and-Veterans-Affairs/Military-Installations-Ranges-and-Training-Areas/wcc7-57p3)
 * __Data Files__ data/military_bases
