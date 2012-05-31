#!/usr/bin/env python
# coding: utf-8

import csv
import string
import jinja2
from settings import macs, orden, colors

loader = jinja2.FileSystemLoader('.', encoding='utf-8')
env = jinja2.Environment(loader=loader)
t = env.get_template('template_msc.txt')

HOSTS = {}

class Host:
    def __init__(self, name):
        self.name = name
        self.label = name
        self.interfaces = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Interface:
    def __init__(self, id):
        self.id = id
        self.letra = None
        self.host = None
        self.color = 'black'

    def __str__(self):
        return " - ".join((self.id, str(self.host)))

    def __repr__(self):
        return self.__str__()


def get_host(name):
    if name not in HOSTS.keys():
        return Host(name)
    else:
        return HOSTS[name]

def set_host(host):
    HOSTS[host.name] = host

f = open('captura', 'r')

csv_r = csv.DictReader(f)
paquetes = list(csv_r)
interfaces = []

dict_template = {'interfaces': [], 'hosts':[]}

for mac in orden['mac']:
    name = macs[mac]
    host = get_host(name)
    i = Interface(mac)
    host.interfaces.append(i)

    i.label = "%s" % i.id[-5:]
    i.host = host
    i.color = colors.get(i.id)
    i.letra = string.letters[len(interfaces)]
    interfaces.append(i)

    dict_template['hosts'].append(host)
    set_host(host)

for i in interfaces:
    dict_template['interfaces'].append(i)
    for idx, msj in enumerate(paquetes):
        if i.id == msj['Mac_src']:
            msj['i_src'] = i
        if i.id == msj['Mac_dst'] or i.host.name == msj['Mac_dst']:
            msj['i_dst'] = i

dict_template['mensajes'] = paquetes

temp_file = open('salida.msc', 'w')

data_output = t.render(dict_template)
temp_file.write(data_output.encode('utf-8'))
temp_file.close()

exit(0)

