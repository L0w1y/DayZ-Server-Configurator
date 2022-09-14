import os
# folders
server_location = str
profiles_location = str
mods_location = str
presets_location = str
firstStart = bool


def OnFirstStart(server_path):
    #checks server folders
    if os.path.exists(f"{server_path}\\mods") and os.path.exists(f"{server_path}\\presets") and os.path.exists(f"{server_path}\\profiles"):
        # print("Server files is initialized")
        return True
    else:
        # print("Some folders are missing...")
        if not(os.path.exists(f"{server_path}\\mods")):
            # print("Missing : MODS")
            os.mkdir(f"{server_path}\\mods")
            mods_location = f"{server_path}\\mods"
        if not(os.path.exists(f"{server_path}\\presets")):
            # print("Missing : PRESETS")
            os.mkdir(f"{server_path}\\presets")
            presets_location = f"{server_path}\\presets"
        if not(os.path.exists(f"{server_path}\\profiles")):
            # print("Missing PROFILES")
            os.mkdir(f"{server_path}\\profiles")
            profiles = f"{server_path}\\profiles"
OnFirstStart("C:\\Users\E82Y\PycharmProjects\DayZ-Server-Configurator\data\\tests\\first start tests")