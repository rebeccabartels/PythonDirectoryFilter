import os
import sys

fileName = "" 
folder_path = os.path.join("/home/riley/CY0420", fileName)

#for root, dirs, files in os.walk(folder_path): 
#    print("All Work and No Play Makes Jack A Dull Boy")
All_Paths = list()
Patters = ["/solved", "/Solved", "/SOLVED", ""]


for root, dirs, files in os.walk("/home/riley/CY0420"):
    for file_name in files:
        current_file_path = os.path.join(root, file_name)
        #print(current_file_path)
        #print(root)
        #print(dirs)
        #print(files)
        #current_week = open(current_file_path, "r")
        #print("SUCCESS")
        if file_name in os.listdir("/home/riley/CY0420"):
            
            #set target as current file path so that we can add it / manipulate it 

            target_dir = current_file_path
            print("TARGET: " + str(current_file_path)) 
            #add the current target / current file path to the All_Paths array for storage 
            All_Paths.append(current_file_path) 
#print("This All the Paths:" + " " + str(All_Paths))

            


#Must clear the array after every program run 
All_Paths = []
print("EMPTY: " + str(All_Paths))

target_dir = current_file_path




#find ./CY0420  -iwholename */solved* > excludefiles
        
        
#keywords to filter out: solution, solved, student guide, lesson plan, .gitattributes, units 4- the rest 


