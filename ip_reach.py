import sys
import subprocess

def ip_reach(list):
    for ip in list:
        ip = ip.rstrip("\n")

        ping_reply = subprocess.call('ping %s -n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
        else:
            print("\n* {} is unreachable :( Check connectivity and try again\n".format(ip))
            sys.exit()