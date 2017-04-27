import os
import json
import re
import fileinput

root = 'C:/Users/kevgil01/Documents/mbed/mbed-os/targets'
target_list = 'C:/Users/kevgil01/Documents/mbed/mbed-os/targets/switch-enabled-targets.log'
old_names = ['SW', 'BUTTON', 'BTN']
targets = []

#raw_file = open(root+'/targets.json', 'r')
#json_f = json.loads(raw_file.read(-1))
#for i in json_f.keys():
#   versions = json_f.get(i).get("release_versions")
#   if(versions is not None):
#       print(i)
#       targets.append(i)

with open(target_list) as file:
    for line in file:    
        device = line.split('/PinNames')[0][2:]
        if(device not in targets):
            targets.append(device)

print(targets)
print("\n")


for target in targets:
    count = 0
    button_instance = 1
    content = []
    lines = []
    with open(root+'/'+target+'/PinNames.h', 'r+') as file:
        for line in file:
            line2 = re.findall(r'SW', line)
            if line2:
                print(count)
                print(line)
                token = line.replace(' ', '').split('=')[0]
                newline = '    BUTTON' + str(button_instance) + ' = ' + token + ',\n'
                print(newline)
                button_instance += 1
                content.append(newline)
                lines.append(count)
            count += 1
        print(content)

    count = 0
    for line in fileinput.FileInput(root+'/'+target+'/PinNames.h', inplace=1):
        if count == lines[-1] + 1:
            for addition in content:
                print(addition, end='')
        count += 1
        print(line, end='')

print('ta-da')