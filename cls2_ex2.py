#!/usr/bin/env python

import telnetlib
import time
import socket
import sys


def send_command(connection, cmd):
    ''' sends command down telnet channel and returns response. '''
    cmd = cmd.rstrip()
    connection.write(cmd + '\n')
    time.sleep(1)
    return connection.read_very_eager()

TELNET_PORT = 23
TELNET_TIMEOUT = 5
IP_ADDR = '184.105.247.70'
username = 'pyclass'
password = '88newclass'

connection = telnetlib.Telnet(IP_ADDR, TELNET_PORT, TELNET_TIMEOUT)

connection.read_until('sername:', TELNET_TIMEOUT)
connection.write(username + '\n')
connection.read_until('ssword:', TELNET_TIMEOUT)
connection.write(password + '\n')

output = send_command(connection, 'show ip int brief')

print output

