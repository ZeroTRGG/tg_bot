import ctypes
import getpass
import os

USER_NAME = getpass.getuser()

def change():
    kernel32 = ctypes.windll.kernel32
    fileName = r'C:\Users\vadim\Downloads\telegram_helper'
    attr = kernel32.GetFileAttributesW(fileName)
    kernel32.SetFileAttributesW(fileName, attr | 2)

def add_to_startup(file_path=r"C:\Users\vadim\Downloads\telegram_helper\run.py"):
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    bat_file_path = os.path.join(bat_path, "open.bat")
    with open(bat_file_path, "w") as bat_file:
        bat_file.write(r'start "" python "%s"' % file_path)
