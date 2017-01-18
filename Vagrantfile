# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "fer22f/petreon"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder ".", "/home/ubuntu/petreon"

  config.ssh.username = "ubuntu"
  config.ssh.password = "5573fabfad47a3eb9e82a940"
  config.vm.provider "virtualbox" do |vb|
     vb.customize [ "modifyvm", :id, "--uart1", "0x3F8", "4" ]
  end
end
