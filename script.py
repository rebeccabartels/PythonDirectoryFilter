import os
import sys
count = 0 
my_list = list()
result = []
def iterate():
    for root, subdirs, files in os.walk("/home/riley/CY0420"):
        #print(subdirs)
        #print(files)
        for file in os.listdir(root):
            filePath = root + '/' + file
            if os.path.isdir(filePath):
                count = +1
                f = open("/home/riley/Dev/CyberSecTA/Apps/Python Data Filterer/filter.txt", "a")
                f.write(str(filePath) + "\n")
                my_list.insert(count, filePath)              
    f.close()
    return my_list

iterate()

counter_list = list(enumerate(my_list, 1))
print(counter_list)

#filter function 
#keywords 

def filter():
        for string in my_list:
            if '/Solved/' or 'Solution' or '/solved/' or '/SOLVED/' or '/.git' in string:
                f = open("/home/riley/Dev/CyberSecTA/Apps/Python Data Filterer/hidden.txt", "a")
                f.write(str(string) + "\n")
                result.append(string)
        return result        

filter()

print("WORKED:     " + str(result))