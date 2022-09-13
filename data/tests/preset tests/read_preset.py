import os
import easygui
from os import listdir
from os.path import isfile, join
# presetpath = easygui.diropenbox(default="C:\\Users\E82Y\PycharmProjects\DayZ-Server-Configurator\data\\tests\preset tests\presets")
presetpath = "C:\\Users\E82Y\PycharmProjects\DayZ-Server-Configurator\data\\tests\preset tests\presets"
for i in os.listdir(presetpath):
    with open(f"{presetpath}\\{i}", "r") as reader:
        line = reader.readlines()
        for i in line:
            print(line[line.index(i)])