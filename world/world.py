import mapnik

m = mapnik.Map(600, 300, "+proj=latlong +datum=WGS84")

m.background = mapnik.Color('steelblue')

s = mapnik.Style()

r = mapnik.Rule()
r.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9')))
r.symbols.append(mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1))
s.rules.append(r)

m.append_style('My Style', s)

lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
lyr.datasource = mapnik.Shapefile(file='/Users/ncanzone/development/mapnik_examples/data/world_borders/world_borders')
lyr.styles.append('My Style')

m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())

mapnik.render_to_file(m, 'world.png', 'png')

