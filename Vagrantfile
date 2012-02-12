Vagrant::Config.run do |all_config|
  all_config.vm.define :mapnik_box do |config|
    # Every Vagrant virtual environment requires a box to build off of.
    config.vm.box = "base_redux"

    # Forward a port from the guest to the host, which allows for outside
    # computers to access the VM, whereas host only networking does not.
    config.vm.forward_port 8000, 8000

    config.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = "~/development/cookbooks"
      chef.add_recipe "mapnik_demo"
    end
  end
end
