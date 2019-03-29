# -*- mode: ruby -*-
Vagrant.configure("2") do |config|
  config.vbguest.iso_path = "#{ENV['HOME']}/Downloads/VBoxGuestAdditions_6.0.0.iso"
  config.vbguest.no_remote = true
  config.vbguest.auto_update=false

  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true

  config.vm.box = "ubuntu/bionic64"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.name = "singularity builder"
    vb.memory = "2096"
    vb.customize ["modifyvm", :id, "--mouse", "usb", "--clipboard", "bidirectional"]
  end
  
  config.vm.provision "shell", inline: <<-SHELL

    #Firewall
    apt-get install ufw --quiet --assume-yes
    ufw default deny incoming
    ufw default allow outgoing
    ufw allow 22/tcp
    echo y | ufw enable
    
#    #General upgrade
    apt-get update --quiet --assume-yes
    apt-get upgrade --quiet --assume-yes

    #Virtualbox v6.0
    wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | apt-key add -
    wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | apt-key add -
    add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian bionic contrib"
    apt-get update
    apt-get install virtualbox-6.0 --quiet --assume-yes

    apt-get install build-essential --quiet --assume-yes
    apt-get install git --quiet --assume-yes
    apt-get install file --quiet --assume-yes
    apt-get install curl --quiet --assume-yes
    apt-get install python3-pip  --quiet --assume-yes
    pip3 install jinja2 --no-cache-dir --disable-pip-version-check

    apt-get install singularity-container --quiet --assume-yes
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    cd /home/vagrant
    git clone https://github.com/seretol/sanger-pathogen-singularity
    cd sanger-pathogen-singularity
    ./build_images.py
    cp *.simg /vagrant
  SHELL
end
