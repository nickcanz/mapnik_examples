import mapnik

m = mapnik.Map(4500, 4500, "+proj=latlong +datum=NAD83")

m.background = mapnik.Color('steelblue')

s = mapnik.Style()

r = mapnik.Rule()
r.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9')))
r.symbols.append(mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1))
s.rules.append(r)

where_filter = "[FCODE] = 1820"
filter_rule = mapnik.Rule()
filter_rule.filter = mapnik.Filter(where_filter)
filter_rule.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('#FF0')))
filter_rule.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#FF0'),0.1))
s.rules.append(filter_rule)

m.append_style('My Style', s)

lyr = mapnik.Layer('world', "+proj=latlong +datum=NAD83")
lyr.datasource = mapnik.Shapefile(file='data/philly_buildings/PhiladelphiaBuildings200712')
lyr.styles.append('My Style')

m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())

mapnik.render_to_file(m, 'images/philly_buildings.png', 'png')
