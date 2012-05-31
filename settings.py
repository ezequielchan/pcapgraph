COLOR_1 = 'red'
COLOR_2 = 'green'
COLOR_3 = 'orange'
COLOR_4 = 'blue'

hosts_macs = (('Router A' ,'EdimaxTe_c6:b5:18'),
              ('Router A' ,'Giga-Byt_63:54:91'),
              ('Router B' ,'EdimaxTe_c6:b3:41'),
              ('Router B' ,'Giga-Byt_68:a0:74'),
              ('Router C' ,'Netronix_aa:35:6f'),
              ('Router C' ,'Giga-Byt_69:65:54'),
              ('Web 1'    ,'Giga-Byt_68:66:c2'),
              ('Web 2'    ,'Giga-Byt_65:cd:be'),
              ('Proxy'    ,'Giga-Byt_68:6f:e0'),
              ('Usuario'  ,'Giga-Byt_69:40:4d'),
              ('Broadcast','ff:ff:ff:ff:ff:ff'))

colors = { 'EdimaxTe_c6:b5:18':COLOR_1,
           'Giga-Byt_63:54:91':COLOR_2,
           'EdimaxTe_c6:b3:41':COLOR_3,
           'Giga-Byt_68:a0:74':COLOR_2,
           'Netronix_aa:35:6f':COLOR_4,
           'Giga-Byt_69:65:54':COLOR_3,
           'Giga-Byt_68:66:c2':COLOR_1,
           'Giga-Byt_65:cd:be':COLOR_1,
           'Giga-Byt_68:6f:e0':COLOR_3,
           'Giga-Byt_69:40:4d':COLOR_4}

orden = {'mac': [],
         'host': []}

hosts = {}
macs = {}

for host, mac in hosts_macs:
    # por HOSTS
    h = hosts.get(host, [])
    h.append(mac)
    hosts[host] = h
    # Por Mac
    macs[mac] = host
    # Orden
    orden['mac'].append(mac)
    orden['host'].append(host)


