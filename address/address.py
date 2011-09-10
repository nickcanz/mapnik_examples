import mapnik

#base map setup
m = mapnik.Map(2500, 2500, "+proj=latlong +datum=NAD83")
m.background = mapnik.Color('#111')

#base line styles
r = mapnik.Rule()
r.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#FFF'),0.1))

#line styles for blocks 0 to 100
where_filter = "([LFROMADDI] <= 100 and [LFROMADDI] > 0) or ([RFROMADDI] <= 100 and [RFROMADDI] > 0)"
filter_rule = mapnik.Rule()
filter_rule.filter = mapnik.Filter(where_filter)
filter_rule.symbols.append(mapnik.LineSymbolizer(mapnik.Color('#cb50ee'),0.5))

#adding styles
s = mapnik.Style()
s.rules.append(r)
s.rules.append(filter_rule)
m.append_style('My Style', s)

#add shape information for specific cities
inputs = [
  ("../data/philly/tl_2010_42101_edges",    "../images/philly.png"),
  ("../data/portland/tl_2010_41051_edges",  "../images/portland.png"),
  ("../data/newyork/tl_2010_36061_edges",   "../images/newyork.png"),
  ("../data/boston/tl_2010_25025_edges",    "../images/boston.png"),
]

def make_map(shpfile, img_name):
  lyr = mapnik.Layer('world', "+proj=latlong +datum=NAD83")
  lyr.datasource = mapnik.Shapefile(file=shpfile)
  lyr.styles.append('My Style')
  m.layers.append(lyr)
  m.zoom_to_box(lyr.envelope())
  mapnik.render_to_file(m, img_name, 'png')

for shpfile, img_name in inputs:
  make_map(shpfile, img_name)
