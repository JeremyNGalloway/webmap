#!/usr/bin/env python

"""
Reads in an nmap generated XML report and outputs a list of URLs

"""

import sys
import xml.etree.ElementTree as et


def main():
    """
    Opens XML file, parses it, and prints formatted output of IPs with their
    list of open ports.
    
    """

    with open(sys.argv[1], 'r') as f:
        root = et.parse(f).getroot()
    
    host_list = []
    for host in root.iter('host'):
        host_d = {'IP': '', 'open_ports': []}
        host_d['IP'] = host.find('address').get('addr')
        for port in host.iter('port'):
            host_d['open_ports'].append(port.get('portid'))
        host_list.append(host_d)

    with open(sys.argv[2], 'w') as h:
    	for host_d in host_list:
       	 for port in host_d['open_ports']:
           	 sys.stdout.write(host_d['IP'] + ':' + port + '\n')
           	 h.write(host_d['IP'] + ':' + port + '<br>' + '<a href="http://' + host_d['IP'] + ':' + port + '''">HTTP</a><br>''' + '\n')
           	 h.write('<a href="http://' + host_d['IP'] + ':' + port + '''">HTTPS</a><br><br>''' + '\n')  
       	 sys.stdout.write('\n')


# If called on the command-line as a script, launch main function.
if __name__ == "__main__":
    main()