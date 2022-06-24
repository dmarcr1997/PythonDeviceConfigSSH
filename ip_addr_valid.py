import sys

def ip_addr_valid(list):
    for ip in list:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')

        if __octet_valid(octet_list):
            continue
        else:
            print("\n* There was an invalid IP address in the file: {} :(\n".format(ip))
            sys.exit()


def __octet_valid(oct):
    return (len(oct) == 4) and (1 <= int(oct[0]) <= 223) and (int(oct[0]) != 127) and (int(oct[0]) != 169 or int(oct[1]) != 254) and (0 <= int(oct[1]) <= 255 and 0 <= int(oct[2]) <= 255 and 0 <= int(oct[3]) <= 255)