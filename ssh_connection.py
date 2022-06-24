import paramiko
import os.path
import time
import sys
import re

user_file = input("\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")

if os.path.exists(user_file):
    print("\n* Username/password file is valid :)\n")
else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()

cmd_file = input("\n# Enter command file path and name (e.g. D:\MyApps\mycmd.txt): ")

if os.path.exists(cmd_file):
    print("\n* Command file is valid :)\n")
else:
    print("\n* Command file {} does not exist :( Please check and try again \n".format(cmd_file))
    sys.exit()