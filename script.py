import os
fileName = "" 
folder_path = os.path.join("/home/riley/CY0420", fileName)

for root, dirs, files in os.walk(folder_path): 
    print("All Work and No Play Makes Jack A Dull Boy")

for root, dirs, files in os.walk("/home/riley/CY0420"):
    for file_name in files:
        current_file_path = os.path.join(root, file_name)
        print(current_file_path)
        print(root)
        print(dirs)
        print(files)
        current_week = open(current_file_path, "r")
        print("SUCCESS")
        current_week.close()    
        
        
#keywords to filter out: solution, solved, student guide, lesson plan, .gitattributes, units 4- the rest 


