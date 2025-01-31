#!/usr/bin/env python3

#Author ID: 162458210


import subprocess
import sys

def free_space():
    if len(sys.argv) > 1:
        return
    
    p = subprocess.Popen("df -h | grep '/$'|awk '{print $4}' ",
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    output, _ = p.communicate()
    return output.decode('utf-8').strip()

print(free_space())