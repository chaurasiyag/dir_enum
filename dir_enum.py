from socket import gethostbyname
import requests
import sys
from os.path import exists
import os


def check_len():
    if len(sys.argv) == 3:
        return True
    else:
        return False


def get_ip(name):
    try:
        ip_ = gethostbyname(name)
        return ip_
    except:
        print("Wrong IP Address or Web Link")
        sys.exit(1)


def check_file_existence():
    if '/' in sys.argv[1] or '\\' in sys.argv[1]:
        _path = sys.argv[1]
    else:
        _path = os.getcwd()+'/'+sys.argv[1]
    if exists(_path):
        return True
    return False


if check_len():
    if check_file_existence():
        ip_ = get_ip(sys.argv[2])

        if '/' in sys.argv[1] or '\\' in sys.argv[1]:
            _path = sys.argv[1]

        else:
            _path = os.getcwd()+'/'+sys.argv[1]

        try:
            sub_list = open(_path).read()
        except:
            print("Enter correct file")
            sys.exit(1)
        directory = sub_list.splitlines()
        n = len(directory)
        count = 0
        for dir in directory:
            dir_enum = f"http://{ip_}/{dir}.html"
            r = requests.get(dir_enum)
            count += 1

            per = int((count/n)*100)
            print('\r', end='', flush=True)
            print(f"{per}% Completed", flush=True, end='')
            if r.status_code != 404:
                print("\nValid Directory :", dir_enum, flush=False)
        else:
            print("Enter valid ip address")
    else:
        print("File doesn't exists")
else:
    print("Provide correct argument of file and host(ip)")
    print(f"{sys.argv[0]} file.txt ip[host]")
    sys.exit(1)
