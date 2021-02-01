elasticsearch role
=========
[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/ansible-role-elasticsearch/master/LICENSE)
[![Build Status](https://travis-ci.org/lean-delivery/ansible-role-elasticsearch.svg?branch=master)](https://travis-ci.org/lean-delivery/ansible-role-elasticsearch)
[![Build Status](https://gitlab.com/lean-delivery/ansible-role-elasticsearch/badges/master/pipeline.svg)](https://gitlab.com/lean-delivery/ansible-role-elasticsearch)
[![Galaxy](https://img.shields.io/badge/galaxy-lean__delivery.elasticsearch-blue.svg)](https://galaxy.ansible.com/lean_delivery/elasticsearch)
![Ansible](https://img.shields.io/ansible/role/d/30177.svg)
![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F30177%2F&query=$.min_ansible_version)

## Summary

This Ansible role has the following features:

 - Install elasticsearch

Requirements
------------

 - This role requires java to be installed. Oracle-java role can be used but open-jdk is also an option.
 - Version of the ansible for installation: 2.9
 - **Supported OS**:  
   - EL
     - 6
     - 7
   - Ubuntu
     - 16.04
     - 18.04
   - Debian
     - 9

SELinux
------------

No problems in role with active SELinux were encountered. In a case of any issues you should [disable SELinux Temporarily or Permanently](https://www.tecmint.com/disable-selinux-temporarily-permanently-in-centos-rhel-fedora/).

## Role Variables

- `es_config`
All Elasticsearch configuration parameters are supported. This is achieved using a configuration map parameter `es_config` which is serialized into the elasticsearch.yml file.
The use of a map ensures the Ansible playbook does not need to be updated to reflect new/deprecated/plugin configuration parameters.
- `elastic_branch`
Is used to select main Elasticsearch branch to be installed (6.x or 7.x current stable versions). By default this variable is set to `6`. So, 6.x version is installed by default. You can override this by setting this variable in playbook.
- `es_version`
Used to define full Elasticsearch version (e.g. 6.6.0). Depends on `elastic_branch` by default. Default value is `6.x`
- `elasticsearch_host`
Specifies the address to which the elasticsearch server will bind. The default is `localhost`,which usually means remote machines will not be able to connect. To allow connections from remote users, set this parameter to a non-loopback address.
- `elasticsearch_port`
Port on which elasticsearch listen to incoming requests. Default value is `9200`.
- `elasticsearch_xmx`
Specifies the maximum memory allocation pool for a JVM. Default value `512m`.
- `elasticsearch_xms`
Specifies the initial memory allocation pool for a JVM. Default value `512m`.
- `es_jvm_custom_parameters`
Custom JVM parameters can be added as a list. These values will be added to jvm.options configuration file.
- `elasticsearch_scripts_install`
Installs custom scripts to work with indices. Default to `false`.
- `elasticsearch_scripts_path`
Path to custom scripts directory. Default is `/opt/es_scripts`.
- `elasticsearch_set_settings`
Define if custom settings should be deployed or default setting is used. Default to `true`.
- `es_restart_on_change`
Configure service restart on configuration upgrade. Default is set to `true`.
- `es_start_service`
Start service after install. Default to `true`.
- `m_lock_enabled`
Configure memory lock. Default to `false`.
- `es_home`
Path to elasticsearch home directory. Default to `/usr/share/elasticsearch`.
- `es_pid_dir`
Path to elasticsearch pid directory. Default to `/var/run/elasticsearch`.
- `es_log_dir`
Path to elasticsearch log directory. Default to `/var/log/elasticsearch`.
- `es_conf_dir`
Path to elasticsearch configuration directory. Default to `/etc/elasticsearch`.
- `es_data_dirs`
Path to elasticsearch data directory. Default to `/var/lib/elasticsearch`.
- `es_basename`
Base name of the service. Used in service configuration files. Default to `elasticsearch`.
- `es_max_open_files`
Maximum number of open files, defaults to `65535`.
- `es_max_map_count`
Maximum number of memory map areas a process may have. Default set to `262144`.
- `es_apt_url`
Path to official Elastic APT repository. Default to `deb https://artifacts.elastic.co/packages/{{ es_repo_name }}/apt stable main`
- `es_yum_url`
Path to official Elastic RPM repository. Default to `https://artifacts.elastic.co/packages/{{ es_repo_name }}/yum`
- `es_repo_file`
Configure repo header. Default to `elastic-{{ es_major_version }}`
- `elastic_gpg_key`
GPG-key from elasticsearch repository. Default value is `https://artifacts.elastic.co/GPG-KEY-elasticsearch`.
- `es_use_oss_version`
Installs open source software version (contains only features that are available under the Apache 2.0 license). Default to `false`

## Advanced Role Variables (Defined in vars/main.yml and {{ ansible_os_family }}.yml)

- `es_major_version`
Used to define Elasticsearch major version. Depends on `elastic_branch` by default. Default value is `6.x`
- `es_user`
The user to run as, defaults to `elasticsearch`
- `es_group`
The group to run as, defaults to `elasticsearch`
- `es_package_name`
Specifies the package name during installation. There is an option to choose open source version. Default to `{{ es_use_oss_version | ternary("elasticsearch-oss", "elasticsearch") }}`
- `es_repo_name`
Specifies Elasticsearch version during adding repository. There is an option to choose open source version. Default to `{{ es_use_oss_version | ternary("oss-" + es_major_version, es_major_version) }}`

- `es_default_file_redhat`
Path to elasticsearch defaults file on RedHat. Default to `/etc/sysconfig/elasticsearch`.
- `es_default_file_debian`
Path to elasticsearch defaults file on Debian. Default to `/etc/default/elasticsearch`.

## Some examples of the installing current role

Dependencies
------------

Java role is presumed as dependency:
https://galaxy.ansible.com/lean_delivery/java

Example Playbook
----------------

### Installing elasticsearch 6.x version:
```yaml
- name: Install Elasticsearch 7.x
  hosts: localhost
  roles:
    - role: lean_delivery.java
    - role: lean_delivery.elasticsearch
  vars:
    elastic_branch: 7
```

### Installing multi node solution with elasticsearch 6.x version:

Playbook structure:

```yaml
.
├── elastic_cluster_inventory
├── group_vars
│   ├── all.yml
│   ├── controller.yml
│   └── dm.yml
└── elastic_cluster.yml
```

elastic_cluster_inventory:

```yaml
[controller]
node1

[dm]
node2
node3
node4

[cluster:children]
controller
dm
```

group_vars/controller.yml:

```yaml
kibana_host: '{{ ansible_host }}'
es_config: 
  node.name: '{{ ansible_host }}'
  cluster.name: my_cluster
  network.host: [_local_,_site_]
  node.master: false
  node.data: false
  node.ingest: false
  discovery.zen.minimum_master_nodes: 2
  discovery.zen.ping.unicast.hosts: '{{ cluster_list }}'
```

group_vars/dm.yml:

```yaml
es_config:
  node.name: '{{ ansible_host }}'
  cluster.name: my_cluster
  network.host: [_local_,_site_]
  node.master: true
  node.data: true
  discovery.zen.minimum_master_nodes: 2
  discovery.zen.ping.unicast.hosts: '{{ cluster_list }}'
```

elastic_cluster.yml:

```yaml
- name: Install elasticsearch and configure cluster
  hosts: all
  vars:
    cluster_list: "{{ groups['cluster'] | map ('extract', hostvars, ['ansible_hostname']) |  join (',') }}"

  roles:
   - role: lean_delivery.java
   - role: lean_delivery.elasticsearch

- name: Install kibana on controller node
  hosts: controller

  roles:
    - role: lean_delivery.kibana
```

License
-------

Apache

Author Information
------------------

authors:
  - Lean Delivery <team@lean-delivery.com>
