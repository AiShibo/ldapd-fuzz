# FreeBSD port of OpenBSD ldapd

ldapd is a daemon which implements version 3 of the LDAP protocol.

A running ldapd process can be controlled using the ldapctl(8) utility.

http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.sbin/ldapd/

## Installation

### Requirements
* libressl

```
make
cd src/regress/usr.sbin/ldapd/ && make
cd - && make install
```

## Usage

`ldapd -f etc/examples/ldapd.conf`

## Status

master | develop
-------|--------
[![Build Status](https://cipier.net/status/koue/ldapd/master)](https://cipier.net/status/koue/ldapd/master) | [![Build Status](https://cipier.net/status/koue/ldapd/develop)](https://cipier.net/status/koue/ldapd/develop)
