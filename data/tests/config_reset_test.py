import sys, os
sname = "Unamad"
passwd = 10203946
passwdadmin = 0000

config = f'hostname = "{sname}";\npassword = "{passwd}";\npasswordAdmin = "{passwdadmin}";\n'

def UpdateConfig(cfg):
    with open("ServerDZ.cfg", "w") as config_file:
        config_file.write(cfg)
UpdateConfig(config)