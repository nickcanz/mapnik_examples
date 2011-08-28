import mapnik
mapfile = "population.xml"
m = mapnik.Map(1400, 600)
mapnik.load_map(m, mapfile)
bbox = mapnik.Envelope(mapnik.Coord(-180.0, -75.0), mapnik.Coord(180.0, 90.0))
m.zoom_to_box(bbox) 
mapnik.render_to_file(m, 'world_population.png', 'png')
