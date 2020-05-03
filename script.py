import os
import sys

fileName = "" 
folder_path = os.path.join("/home/riley/CY0420", fileName)

for root, dirs, files in os.walk("/home/riley/CY0420"):
    for file_name in files:
        current_file_path = os.path.join(root, file_name)
        if file_name in os.listdir("/home/riley/CY0420"):  #set target as current file path so that we can add it / manipulate it 
            f = open("/home/riley/Dev/CyberSecTA/Apps/Python Data Filterer/filter.txt", "a")
            f.write(str(current_file_path) + "\n")
            print(f)
            
    f.close()
        
#keywords to filter out: solution, solved, student guide, lesson plan, .gitattributes, units 4- the rest 