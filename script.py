import os
import sys


def collect_user_information():
    # Prompt the user for their username
    filter1 = input("What do you wish to filter? ")
    filter2 = input("What do you wish to filter? ")
    filter3 = input("What do you wish to filter? ")
    # The list that will store all of the user's data inside of it
    user_info = [filter1, filter2, filter3]

    # Return a list with username, email, and password
    return user_info
count = 0
for root, subdirs, files in os.walk("/home/riley/CY0420"):
    #print(root)
    #print(subdirs)
    #print(files)
    for file in os.listdir(root):
        filePath = root + '/' + file
        if os.path.isdir(filePath):
            f = open("/home/riley/Dev/CyberSecTA/Apps/Python Data Filterer/filter.txt", "a")
            f.write(str(filePath) + "\n")
            count += 1
        else:
            print(count)
f.close()
