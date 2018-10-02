import os

import testinfra.utils.ansible_runner

group_name = 'ansible_role_elasticsearch_v6_centos'

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts(group_name)


def test_elasticsearch_package_is_installed(host):
    elasticsearch_pkg = host.package("elasticsearch")
    assert elasticsearch_pkg.is_installed
    assert elasticsearch_pkg.version.startswith("6")


def test_elasticsearch_service_running_and_enabled(host):
    elasticsearch_svc = host.service("elasticsearch")
    assert elasticsearch_svc.is_running
    assert elasticsearch_svc.is_enabled
