import os
import sys

for root, subdirs, files in os.walk("/home/riley/CY0420"):
    #print(root)
    #print(subdirs)
    #print(files)
    for file in os.listdir(root):
        filePath = root + '/' + file
        if os.path.isdir(filePath):
            f = open("/home/riley/Dev/CyberSecTA/Apps/Python Data Filterer/filter.txt", "a")
            f.write(str(filePath) + "\n")
            print(filePath)
        else:
            print(filter)
f.close()
