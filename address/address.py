import mapnik

m = mapnik.Map(1500, 1500, "+proj=latlong +datum=NAD83")

m.background = mapnik.Color('#000000')

s = mapnik.Style()

r = mapnik.Rule()
#r.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9')))
r.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#FFFFFF'),0.1))
s.rules.append(r)

m.append_style('My Style', s)

lyr = mapnik.Layer('world', "+proj=latlong +datum=NAD83")
lyr.datasource = mapnik.Shapefile(file='/Users/ncanzone/development/mapnik_examples/address/philly/tl_2010_42101_edges')
lyr.styles.append('My Style')

m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())

mapnik.render_to_file(m, 'address.png', 'png')
