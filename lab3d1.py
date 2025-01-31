#!/usr/bin/env python3

'''
import os
os.system('ls')
os.system('whoami')
os.system('ifconfig')

ls_return = os.system('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.system('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)

ipconfig_return = os.system('ipconfig')
print('The contents of ipconfig_return:',ipconfig_return)
'''

'''
import os
os.popen('ls')
os.popen('whoami')
os.popen('ifconfig')

ls_return = os.popen('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.popen('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.popen('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)

whoami_return=os.popen('whoami')
whoami_contents = whoami_return.read()
print('whoami_contents:',whoami_contents)

ipconfig_return = os.popen('ipconfig')
ipconfig_contents = ipconfig_return.read()
print('The contents of ipconfig_return:',ipconfig_contents)
'''
'''
import subprocess

p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

output = p.communicate()
print(output)
print(output[0])
# The above stdout is stored in bytes
# Convert stdout to a string and strip off the newline characters
stdout = output[0].decode('utf-8').strip()
print(stdout)
'''













'''
def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    
    return output.decode('utf-8').strip()
print(free_space())
'''