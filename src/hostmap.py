# -*- coding: utf-8 -*-
"""边缘节点清单读取。"""
import configparser

DOMAIN = "keetaglobal.com"
INVENTORY = "deploy/inventory/hosts.ini"


def load(path=INVENTORY):
    cp = configparser.ConfigParser()
    cp.read(path, encoding="utf-8")
    out = {}
    for sec in cp.sections():
        if sec == "global":
            continue
        out[sec] = dict(cp[sec])
    return out


def by_role(inv, role):
    return {k: v for k, v in inv.items() if v.get("role") == role}


def fqdn(host):
    return host if host.endswith(DOMAIN) else "%s.%s" % (host, DOMAIN)
