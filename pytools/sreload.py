#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, os, sys, base64
from itertools import cycle

def encrypt(rHost="127.0.0.1", rUsername="user_iptvpro", rPassword="", rDatabase="xtream_iptvpro", rServerID=1, rPort=7999):
    try: os.remove("/home/xtreamcodes/iptv_xtream_codes/config")
    except: pass
    data = '{"host":"%s","db_user":"%s","db_pass":"%s","db_name":"%s","server_id":"%d", "db_port":"%d"}' % (
        rHost, rUsername, rPassword, rDatabase, rServerID, rPort)
    encoded = ''.join(chr(ord(c)^ord(k)) for c,k in zip(data, cycle('5709650b0d7806074842c6de575025b1')))
    with open('/home/xtreamcodes/iptv_xtream_codes/config', 'wb') as rf:
        rf.write(base64.b64encode(encoded.encode()).decode().replace('\n', '').encode())


def start(): 
    os.system("chown xtreamcodes:xtreamcodes /home/xtreamcodes/iptv_xtream_codes/config")
    os.system("chmod 777 /home/xtreamcodes/iptv_xtream_codes/config")
    os.system("/home/xtreamcodes/iptv_xtream_codes/start_services.sh")

if __name__ == "__main__":
    rHost = sys.argv[1]
    rPort = int(sys.argv[2])
    rUsername = sys.argv[3]
    rPassword = sys.argv[4]
    rDatabase = sys.argv[5]
    rServerID = int(sys.argv[6])
    encrypt(rHost, rUsername, rPassword, rDatabase, rServerID, rPort)
    start()