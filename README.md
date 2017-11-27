[![Ansible Role](https://img.shields.io/ansible/role/22414.svg)](https://galaxy.ansible.com/mplachter/cerebro/) [![Build Status](https://travis-ci.org/mplachter/ansible-role-cerebro.svg?branch=master)](https://travis-ci.org/mplachter/ansible-role-cerebro)

# ansible-role-cerebro

This is an ansible role for installing and configuring [cerebro](https://github.com/lmenezes/cerebro).

## Requirements

* Ansible
  * 2.3.2.0 +

##Role Variables

### Cerebro installation configuration

```
----
cerebro_install_dir: /opt
cerebro_version: 0.7.1
cerebro_group: root
cerebro_owner: root
cerebro_port: 9000
cerebro_http_address: 0.0.0.0
```

### Cerebro app configuration

```
cerebro_local_data_path: ./cerebro.db
cerebro_play_secret: ki:s:[[@=Ag?QI`W2jMwkY:eqvrJ]JqoJyi2axj3ZvOv^/KavOT4ViJSv?6YY4[N
cerebro_rest_history: 100

cerebro_es_hosts:
  - name: This Cluster
    host: http://elasticsearch.com
```

### Configuration for LDAP

```
cerebro_ldap_auth:
  url: ldap://host:port
  base_dn: ou=active,ou=Employee
  method: simple
  user_domain: domain.com
  user_auth:
    username: admin
    password: 1234
```

## Dependencies

This role will also install the following Dependencies

* geerlingguy.java
  * jdk 1.8.0

## Example Playbook

```
---
- hosts: all
  become: true
  roles:
    - role: mplachter.cerebro
  vars:
    cerebro_local_data_path: /var/lib/cerebro/cerebro.db
    cerebro_play_secret: ki:s:[[@=Ag?QI`W2jfdsfwkY:eqvrJ]JqoJyi2DCj3Zv0v^/KavOT4ViJdsafY4[N
    cerebro_rest_history: 200

    cerebro_es_hosts:
      - name: Prod Cluster
        host: http://prod.es5.mydomain.com
        es_auth:
          username: ES_user
          password: ES_user_password
      - name: QA Cluster
        host: http://qa.es5.mydomain.com
```

* Minimal Example

```
---
- hosts: all
  become: true
  roles:
    - role: mplachter.cerebro
```

## License

MIT

## Author Information

Matt Plachter
