import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_verify_cerebro_bin(File):
    f = File('/opt/cerebro/bin/cerebro')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_cerebro_config(File, Command):
    f = File('/opt/cerebro/conf/application.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('rest.history.size = 50')
    assert f.contains('data.path = "./cerebro.db"')
    if '-config' in Command("hostname").stdout:
        assert f.contains('host = "http://localhost:9200"')
        assert f.contains('name = "prod_cluster"')


def test_cerebro_running_and_enabled(Service):
    svc = Service("cerebro")
    assert svc.is_running
    assert svc.is_enabled


def test_cerebro_listener(Socket, SystemInfo):
    assert Socket('tcp://127.0.0.1:9000').is_listening
