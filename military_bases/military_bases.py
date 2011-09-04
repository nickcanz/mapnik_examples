import mapnik

m = mapnik.Map(4500, 2500, "+proj=latlong +datum=WGS84")

m.background = mapnik.Color('steelblue')

s = mapnik.Style()

r = mapnik.Rule()
#r.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9')))
r.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#FFF'),0.1))
s.rules.append(r)
m.append_style('My Style', s)

poly_style = mapnik.Style()
poly_rule = mapnik.Rule()
poly_rule.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#FF0')))
poly_style.rules.append(poly_rule)
m.append_style('Poly Style', poly_style)

mil_bases_lyr = mapnik.Layer('mil_bases', "+proj=latlong +datum=WGS84")
mil_bases_lyr.datasource = mapnik.Shapefile(file='/Users/ncanzone/development/mapnik_examples/data/military/MILITARY_INSTALLATIONS_RANGES_TRAINING_AREAS_BND')
mil_bases_lyr.styles.append('My Style')
mil_bases_lyr.styles.append('Poly Style')
m.layers.append(mil_bases_lyr)

state_bounds_lyr = mapnik.Layer('state_bounds', "+proj=latlong +datum=NAD83")
state_bounds_lyr.datasource = mapnik.Shapefile(file='/Users/ncanzone/development/mapnik_examples/data/boundaries/co2000p020')
state_bounds_lyr.styles.append('My Style')
m.layers.append(state_bounds_lyr)

bbox = mapnik.Envelope(mapnik.Coord(-126.914,49.610), mapnik.Coord(-65.083,23.725))

m.zoom_to_box(bbox)

mapnik.render_to_file(m, 'military_bases.png', 'png')
