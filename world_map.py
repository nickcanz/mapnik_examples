import sys
import mapnik
mapfile = "population.xml"

output_file = 'images/world_population.png'
if len(sys.argv) > 1:
  output_file = sys.argv[1]

m = mapnik.Map(1400, 600)
mapnik.load_map(m, mapfile)
bbox = mapnik.Envelope(mapnik.Coord(-180.0, -75.0), mapnik.Coord(180.0, 90.0))
m.zoom_to_box(bbox) 
mapnik.render_to_file(m, output_file, 'png')
