import mapnik

m = mapnik.Map(1500, 1500, "+proj=latlong +datum=NAD83")

m.background = mapnik.Color('#111')

s = mapnik.Style()

r = mapnik.Rule()

r.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#FFF'),0.1))

where_filter = "([LFROMADDI] <= 100 and [LFROMADDI] > 0) or ([RFROMADDI] <= 100 and [RFROMADDI] > 0)"
filter_rule = mapnik.Rule()
filter_rule.filter = mapnik.Filter(where_filter)
filter_rule.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#cb50ee'),0.5))

s.rules.append(r)
s.rules.append(filter_rule)

m.append_style('My Style', s)

lyr = mapnik.Layer('world', "+proj=latlong +datum=NAD83")
lyr.datasource = mapnik.Shapefile(file='/Users/ncanzone/development/mapnik_examples/data/philly/tl_2010_42101_edges')
lyr.styles.append('My Style')

m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())

mapnik.render_to_file(m, 'address.png', 'png')
