# Vagrantgen

Vagrantgen is a simply CLI to generate Vagrantfiles from a standard YAML.

This is a YAML example:

```yml
- projectname: cluster1
  provider: virtualbox
  vms:
  - name: vm01
    box: rockylinux/8
    mem: 1024
    cpu: 2
```

And this the Vagrantfile generated:
```rb
Vagrant.configure("2") do |config|
    config.vm.synced_folder ".", "/vagrant", disabled: true

    config.vm.define "cluster1vm01" do |node|
        node.vm.hostname = "cluster1vm01"
        node.vm.box = "rockylinux/8"
        node.vm.provider "virtualbox" do |provider|
            provider.memory = "1024"
            provider.cpus = "2"
        end
    end
end
```

## How use the CLI

If you run `vagrantgen -h`, then you find the help menu:
```sh
$ vagrantgen -h

usage: vagrantgen [-h] {template,vf,ai} ...

Vagrantfile Generator - github.com/aramcap/vagrantgen

positional arguments:
  {template,vf,ai}  Subcommands
    template        Generate template
    vf              Generate Vagrantfile
    ai              Generate ansible-inventory file from "vagrant ssh-config" command

optional arguments:
  -h, --help        show this help message and exit
```

Any menu has `--help` command available.

- `vagrantgen template`: Generates a template to facilitate the use.
- `vagrantgen vf`: Generates a Vagrantfile from a template file.
  - With argument `-i` you can specify a filename (by default _vagrant-template.yaml_).
  - With argument `-o` the output is in stdout.
  - With argument `-f` the output file is overwriten if exists.
- `vagrantgen ai`: Generates a Ansible inventory file from `vagrant ssh-config` command.
  - With argument `-o` the output is in stdout.
  - With argument `-f` the output file is overwriten if exists.

## Another examples

```yml
- projectname: cluster1
  provider: libvirt # libvirt or virtualbox or docker
  vms:
  - name: vm01
    box: rockylinux/8
    mem: 1024
    cpu: 2
    disks:
    - name: disk1.qcow2
      size: 10G
    net:
    - network: private_network
      ip: 192.168.122.100
    provision:
    - provisioner: ansible
      payload: "playbook.yml"
```

```yml
- projectname: cluster1
  provider: docker # libvirt or virtualbox or docker
  vms:
  - name: vm01
    box: centos-ssh
```

Docker provider not support net tag (ports is optional tag):
```yml
- projectname: cluster1
  provider: docker # libvirt or virtualbox or docker
  vms:
  - name: vm01
    box: centos-ssh
    ports:
      - "10023:23"
```

Example with provision (optional tag):
```yml
- projectname: cluster1
  provider: docker # libvirt or virtualbox or docker
  vms:
  - name: vm01
    box: centos-ssh
    provision:
    - provisioner: shell-inline # shell-inline, shell-external, ansible
      payload: "echo Hello > /home/vagrant/hello; chown vagrant:vagrant /home/vagrant/hello"
```

```yml
- projectname: cluster1
  provider: docker # libvirt or virtualbox or docker
  vms:
  - name: vm01
    box: centos-ssh
    provision:
    - provisioner: ansible # shell-inline, shell-external, ansible
      payload: "playbook.yml"
```

Libvirt or Virtualbox providers not support ports tag:
```yml
- projectname: cluster1
  provider: virtualbox # libvirt or virtualbox or docker
  vms:
  - name: vm01
    box: centos/7
    mem: 1024
    cpu: 2
```

Example with network (optional tag):
```yml
- projectname: cluster1
  provider: virtualbox # libvirt or virtualbox or docker
  vms:
  - name: vm01
    box: centos/7
    mem: 1024
    cpu: 2
    disks:
    - name: disk1.vdi
      size: 20 # GBs
    net:
    - network: private_network
      ip: 192.168.122.100
    - network: public_network
      dev: br01
    - network: forwarded_port
      guest: 80
      host: 8080
      host_ip: 127.0.0.1
```

## Colaborate

If do you want to colaborate, you can make a pull-request on https://github.com/aramcap/vagrantgen.

## License

GNU AFFERO GENERAL PUBLIC LICENSE version 3
