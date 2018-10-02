elasticsearch role
=========
[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/ansible-role-elasticsearch/master/LICENSE)
[![Build Status](https://travis-ci.org/lean-delivery/ansible-role-elasticsearch.svg?branch=master)](https://travis-ci.org/lean-delivery/ansible-role-elasticsearch)
[![Build Status](https://gitlab.com/lean-delivery/ansible-role-elasticsearch/badges/master/build.svg)](https://gitlab.com/lean-delivery/ansible-role-elasticsearch)

## Summary

This Ansible role has the following features:

 - Install elasticsearch

Requirements
------------

 - This role requires java to be installed. Oracle-java role can be used but open-jdk is also an option. 
 - Version of the ansible for installation: 2.5
 - **Supported OS**:  
   - EL
     - 6
     - 7
   - Ubuntu
     - 18.04

SELinux
------------

No problems in role with active SELinux were encountered. In a case of any issues you should [disable SELinux Temporarily or Permanently](https://www.tecmint.com/disable-selinux-temporarily-permanently-in-centos-rhel-fedora/).

## Role Variables

- `es_config`
All Elasticsearch configuration parameters are supported. This is achieved using a configuration map parameter `es_config` which is serialized into the elasticsearch.yml file.
The use of a map ensures the Ansible playbook does not need to be updated to reflect new/deprecated/plugin configuration parameters.
- `elastic_branch`
Is used to select main Elasticsearch branch to be installed (5.x or 6.x current stable versions). By default this variable is set to `5`. So, 5.x version is installed by default. You can override this by setting this variable in playbook.
- `es_major_version`
Used to define Elasticsearch major version. Depends on `elastic_branch` by default. Default value is `5.x`
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
- `es_user`
The user to run as, defaults to `elasticsearch`.
- `es_group`
The group to run as, defaults to `elasticsearch`.
- `es_init_script`
Path to elasticsearch service file if `upstart` is used. Default to `/etc/init.d/elasticsearch`.
- `es_sysd_script`
Path to elasticsearch service file if `systemd` is used. Default to `/usr/lib/systemd/system/elasticsearch.service`.
- `es_max_threads`
Number of thread pools for different types of operations elasticsearch uses. Default value depends on elasticsearch version. For 5.x version the value is set to `2048` and for 6.x version is `8192`.
- `es_max_open_files`
Maximum number of open files, defaults to `65535`.
- `es_max_map_count`
Maximum number of memory map areas a process may have. Default set to `262144`.
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
- `es_default_file_redhat`
Path to elasticsearch defaults file on RedHat. Default to `/etc/sysconfig/elasticsearch`.
- `es_default_file_debian`
Path to elasticsearch defaults file on Debian. Default to `/etc/default/elasticsearch`.
- `elastic_gpg_key`
GPG-key from elasticsearch repository. Default value is `https://artifacts.elastic.co/GPG-KEY-elasticsearch`.

## Some examples of the installing current role

Dependencies
------------

Java role is presumed as dependency:
https://galaxy.ansible.com/lean_delivery/java

Example Playbook
----------------

### Installing elasticsearch 6.x version:
```yaml
- name: Install Elasticsearch 6.x
  hosts: localhost
  roles:
    - role: lean_delivery.java
    - role: elasticsearch
  vars:
    elastic_branch: 6
```

### Installing elasticsearch 5.x version:
```yaml
- name: Install Elasticsearch 5.x
  hosts: localhost
  roles:
    - role: lean_delivery.java
    - role: elasticsearch
```

License
-------

Apache

Author Information
------------------

authors:
  - Lean Delivery <team@lean-delivery.com>
