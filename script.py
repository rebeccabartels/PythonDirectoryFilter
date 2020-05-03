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
#print(counter_list)

#filter function 
#keywords 

def filter():
    for root, subdirs, files in os.walk("/home/riley/CY0420"):
        for file in os.listdir(root):
            filePath = root + '/' + file
            if os.path.isdir(filePath):
                result.append(filePath)
                #print(result)
    return result        

filter()


keyword_list = list()
def keyword():
    x = raw_input("enter a filter: ")
    keyword_list.append(str(x))
    #print "Filtered Data %s " % x
    for elem in result:
        print(elem)
        if str(x) in elem and 'unsolved' not in elem and 'Unsolved' not in elem and 'UNSOLVED' not in elem and '/unsolved' not in elem and '/Unsolved' not in elem and '/UNSOLVED' not in elem:
            f = open("/home/riley/Dev/CyberSecTA/Apps/Python Data Filterer/hidden.txt", "a")
            f.write(str(elem) + "\n")
            keyword_list.append(str(x))

keyword()

print(keyword_list)



