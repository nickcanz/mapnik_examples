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
  FileUtils.rmdir 'images'
  FileUtils.mkdir 'images'
  %w{ address/address.py world/world.py philly_buildings/philly_buildings.py xml_styling/world_map.py military_bases/military_bases.py }.each do |script|
    `python #{script}`
  end
end
