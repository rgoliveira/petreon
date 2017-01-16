# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "fer22f/petreon"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder ".", "/home/ubuntu/petreon"
end
