import os

path = "C:/Users/E82Y/PycharmProjects/DayzServerLoader/data/ui"
for file in os.listdir(path):
    if file.endswith(".ui"):
        os.system(f"python -m Pyqt5.puic5 {os.path.join(path, file)} -o {file}.py")