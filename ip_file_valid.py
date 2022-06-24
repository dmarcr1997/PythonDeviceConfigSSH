import os.path
import sys

def ip_file_valid():
    ip_file = input("\n# Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ")

    if os.path.isfile(ip_file) == True:
        print("\n* IP file is valie :)\n")
    else:
        print("\n* File {} does not exist :( Please check and try again.\n".format(ip_file))
        sys.exit()
    selected_ip_file = open(ip_file, 'r')
    selected_ip_file.seek(0)
    
    ip_list = selected_ip_file.readlines()
    
    selected_ip_file.close()

    return ip_list