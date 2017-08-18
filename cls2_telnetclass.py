#!/usr/bin/env python

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 5


class TelnetConnection(object):
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        self.connection = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)

    def login(self):
        output = self.connection.read_until('sername:', TELNET_TIMEOUT)
        self.connection.write(self.username + '\n')
        output = self.connection.read_until('ssword:', TELNET_TIMEOUT)
        self.connection.write(self.password + '\n')
        time.sleep(1)
        return output

    def send_command(self, cmd="\n"):
        ''' sends command down telnet channel and returns response. '''
        cmd = cmd.rstrip()
        self.connection.write(cmd + '\n')
        time.sleep(1)
        return self.connection.read_very_eager()


def main():
    ip_addr = raw_input("Enter IP Address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = '88newclass'

    new_conn = TelnetConn(ip_addr,username,password)
    new_conn.login()
    new_conn.send_command()

    print "\n"
    print output
    print "\n"


if __name__ == "__main__":
    main()