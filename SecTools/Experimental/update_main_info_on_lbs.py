#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, json, requests, socket

rBasePath = "/home/xtreamcodes/iptv_xtream_codes"
rConfigPath = "%s/config" % rBasePath

def decryptConfig(rConfig):
    try:
        import base64
        from itertools import cycle
        data = base64.b64decode(rConfig).decode('utf-8')
        return json.loads(''.join(chr(ord(c)^ord(k)) for c,k in zip(data, cycle('5709650b0d7806074842c6de575025b1'))))
    except:
        return None

if __name__ == "__main__":
    print(" ")
    print("This tool will update streaming server information on all load balancers.")
    print(" ")
    rConfig = decryptConfig(open(rConfigPath, 'rb').read())
    if rConfig:
        rPassword = ""
        while rPassword == "":
            rPassword = input("Please enter your Live Streaming Password: ")
        rServers = json.loads(os.popen("curl -s 'http://127.0.0.1:25461/system_api.php?password=" + rPassword + "&action=getServers'").read())
        for rServer in rServers:
            if rServer["id"] != int(rConfig["server_id"]):
                rAPI = "http://" + rServer["server_ip"] + ":" + str(rServer["http_broadcast_port"]) + "/system_api.php"
                rData = {"action": "getServers", "password": rPassword, "main": json.dumps({"server_id": rConfig["server_id"], "server_ip": rConfig["host"]})}
                try:
                    rResponse = requests.post(rAPI, data=rData, timeout=5).content
                    print("Sent to Server #" + str(rServer["id"]) + ": " + rServer["server_name"])
                except:
                    print("Failed to send to Server #" + str(rServer["id"]) + ": " + rServer["server_name"])
    else:
        print("Couldn't read config!")
        sys.exit(1)