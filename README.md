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

### Configuration for LDAP or Basic authentication

```
cerebro_auth_basic:
  username: justereseau
  password: templatetempo

cerebro_auth_ldap:
  url: ldap://dc.compagnie.com:389
  # OpenLDAP might be something like "ou=People,dc=domain,dc=com"
  base_dn: ou=People,dc=domain,dc=com
  # Usually method should  be "simple" otherwise, set it to the SASL mechanisms to try
  method: simple #default: simple
  # user-template executes a string.format() operation where
  # username is passed in first, followed by base-dn. Some examples
  # - %s => leave user untouched
  # - %s@domain.com => append "@domain.com" to username
  # - uid=%s,%s => usual case of OpenLDAP
  user-template: d # optional
  # User identifier that can perform searches
  bind_dn: d # optional
  bind_pw: s # optional
  group_search:
    # If left unset parent's base-dn will be used
    base_dn: d
    # Attribute that represent the user, for example uid or mail
    user_attr: q
    # Define a separate template for user-attr
    # If left unset parent's user-template will be used
    user_attr_template: d
    # Filter that tests membership of the group. If this property is empty then there is no group membership check
    # AD example => memberOf=CN=mygroup,ou=ouofthegroup,DC=domain,DC=com
    # OpenLDAP example => CN=mygroup
    group: d
```

## Dependencies

This role will also install the following Dependencies unless the `cerebro_skip_java_install: true` variable is set.

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
