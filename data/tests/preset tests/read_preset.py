import os
# folders
server_location = str
profiles_location = str
mods_location = str
presets_location = str
firstStart = bool
def OnFirstStart(server_path):
    #checks mods folder
    if os.path.exists(f"{server_path}\\mods") and os.path.exists(f"{server_path}\\presets") and os.path.exists(f"{server_path}\\profiles"):
        return True
    else:
        if not(os.path.exists(f"{server_path}\\mods")):
            os.mkdir(f"{server_path}\\mods")
            mods_location = f"{server_path}\\mods"
        if not(os.path.exists(f"{server_path}\\presets")):
            os.mkdir(f"{server_path}\\presets")
            presets_location = f"{server_path}\\presets"
        if not(os.path.exists(f"{server_path}\\profiles")):
            os.mkdir(f"{server_path}\\profiles")
            profiles = f"{server_path}\\profiles"
