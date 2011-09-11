# Mapnik Examples

The purpose of these examples are to give a brief look at what is possible with the [Mapnik library](http://mapnik.org/).

Written for talk that I am giving for [Philly PUG meeting](http://www.meetup.com/phillypug/) on 13 Sept 2011.

## World Borders Example

This is the 'Hello World' of Mapnik, taken from [this Mapnik tutorial](http://trac.mapnik.org/wiki/GettingStarted). The result will be an image displaying the borders of the countries of the world. The data comes from [Mapping Hacks](http://mappinghacks.com/data/).

 * __To Run__ `python world.py`
 * __Output__ images/world.png
 * __Data__ data/world_borders

## World Population Example

This example uses an xml file to specify styling and layers instead writing python code and is taken from [this Mapnik example](http://trac.mapnik.org/wiki/XMLGettingStarted#Step2).

 * __To Run__ `python world_population.py`
 * __Output__ images/world_population.png
 * __Data__ data/world_borders_pop

## Addresses Example

This example is meant to show how geographic data can be used to tell a story. In every city of this example, the addresses that have numbers 0-100 are colored differently. The purpose of this coloring can show how the city grew and expanded. This started from a [post on the Cartogrammer blog](http://www.cartogrammar.com/blog/paint-by-numbers/).

In regards to Mapnik, this example shows how to change the styling of the map based on attributes of a shapefile. The sample data from this example came from [Census Tiger line data](http://www.census.gov/cgi-bin/geo/shapefiles2010/main). Select "All Lines" and then the state and county that you want.

 * __To Run__ `python address.py`
 * __Output__ images/ boston.png, newyork.png, philly.png, portland.png
 * __Data__ data/ boston, newyork, philly, portland
