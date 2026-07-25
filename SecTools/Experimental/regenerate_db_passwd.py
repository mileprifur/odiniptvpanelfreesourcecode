#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, json, random, string
from itertools import cycle

rBasePath = "/home/xtreamcodes/iptv_xtream_codes"
rConfigPath = "%s/config" % rBasePath

def decryptConfig(rConfig):
    try:
        import base64
        data = base64.b64decode(rConfig).decode('utf-8')
        return json.loads(''.join(chr(ord(c)^ord(k)) for c,k in zip(data, cycle('5709650b0d7806074842c6de575025b1'))))
    except:
        return None

def encryptConfig(rConfig):
    import base64
    data = json.dumps(rConfig)
    encoded = ''.join(chr(ord(c)^ord(k)) for c,k in zip(data, cycle('5709650b0d7806074842c6de575025b1')))
    return base64.b64encode(encoded.encode()).decode().replace('\n', '')

def generate(length=23):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

if __name__ == "__main__":
    print(" ")
    print("This tool will regenerate the database password for the panel user.")
    print(" ")
    rConfig = decryptConfig(open(rConfigPath, 'rb').read())
    if rConfig:
        rRet = os.system("mysql -u root -e \"SELECT VERSION()\" >/dev/null 2>&1")
        if rRet == 0:
            rRootPass = ""
        else:
            rRootPass = input("Please enter your MySQL Root Password: ")
        rNewPass = generate()
        os.system("mysql -u root -p" + rRootPass + " -e \"DROP USER '" + rConfig["db_user"] + "'@'%';\" 2>/dev/null")
        os.system("mysql -u root -p" + rRootPass + " -e \"DROP USER '" + rConfig["db_user"] + "'@'localhost';\" 2>/dev/null")
        os.system("mysql -u root -p" + rRootPass + " -e \"CREATE USER '" + rConfig["db_user"] + "'@'%' IDENTIFIED BY '" + rNewPass + "';\" 2>/dev/null")
        os.system("mysql -u root -p" + rRootPass + " -e \"GRANT ALL PRIVILEGES ON *.* TO '" + rConfig["db_user"] + "'@'%' WITH GRANT OPTION;\" 2>/dev/null")
        os.system("mysql -u root -p" + rRootPass + " -e \"FLUSH PRIVILEGES;\" 2>/dev/null")
        rConfig["db_pass"] = rNewPass
        with open(rConfigPath, 'wb') as rf:
            rf.write(encryptConfig(rConfig).encode())
        print("New password: " + rNewPass)
        print("Done!")
    else:
        print("Couldn't read config!")
        sys.exit(1)