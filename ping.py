import sys
import os
import platform
import subprocess

def ping(hostname):
    
    devnull = open(os.devnull, 'w')
    os_type = platform.system()
    
    if os_type == 'Linux' or os_type == 'Darwin':
        modifier = '-c'
    elif os_type == 'Windows':
        modifier = '/n'
    
    response = subprocess.call('ping {} 3 {}'.format(modifier, hostname), stdout = devnull, stderr = devnull)
    if response == 0:
        status = 'online'
    else:
        status = 'offline'
    return hostname, status

if __name__ in '__main__':
    try:
        hostname = sys.argv[1]
        hostname, status = ping(hostname)
        print("{} {}".format(hostname, status))
    except Exception as e:
        print("Ping failed due to the following error, {}".format(e))
    except KeyboardInterrupt:
        print("\nProcess halted by user, Exiting...")
