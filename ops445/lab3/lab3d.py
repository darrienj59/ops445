#!/usr/bin/env python3

# Author ID: [140360199]

import subprocess

def free_space():
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())

