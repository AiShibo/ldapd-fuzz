### Unknown user ldap

```bash
pw useradd ldap -d /var/empty -s /usr/sbin/nologin -c "ldap Daemon"
```

### config file
location: /etc/ldapd.conf
```txt
# $OpenBSD: ldapd.conf,v 1.2 2020/09/19 09:46:35 tb Exp $

schema "/etc/ldap/core.schema"
schema "/etc/ldap/inetorgperson.schema"
schema "/etc/ldap/nis.schema"
schema "/etc/ldap/bsd.schema"

listen on lo0
listen on "/var/run/ldapi"

#namespace "dc=example,dc=com" {
#   rootdn      "cn=admin,dc=example,dc=com"
#   rootpw      "secret"
#   index       sn
#   index       givenName
#   index       cn
#   index       mail
#}
```

### missing ldapd user

```bash
pw useradd ldap -d /var/empty -s /usr/sbin/nologin -c "OpenLDAP Daemon"
```

### missing schema files

The ldapd-port project provide us the schema files located in `ldapd/src/usr.sbin/ldapd/schema`, copy them to the desired location

### First round of fuzzing

Found some crashes, turned out to be a bug in the ported imsg framework. Now archiving the findings to be findings-old and re-run the program

### command used to fuzz the program
```bash
afl-fuzz \
  -i in \
  -o findings \
  -g 4000 \
  -m none \
  -- ./ldapd -d
```
