require 'fileutils'

desc "Get shapefile data used in examples"
task :getdata do
  %x{
  wget http://www.sudobangbang.net/static/data.tar.gz
  tar xzvf data.tar.gz
  rm data.tar.gz
  }
end

desc "Create all map examples"
task :createmaps do
  FileUtils.rm_rf 'images'
  FileUtils.mkdir 'images'
  %w{ address.py world.py philly_buildings.py world_population.py military_bases.py }.each do |script|
    puts "==============Running #{script}=============="
    `python #{script}`
    puts "==============Finished #{script}=============="
  end
end

desc "Start tilelite server"
task :tileserver do
  `liteserv.py -c --processes=2 --cache-path=/tmp/milbases military_bases.xml`
end
