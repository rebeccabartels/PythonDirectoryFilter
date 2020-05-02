#!/usr/bin/env python

import os, sys



class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'



HOMEPATH = os.path.expanduser('~')

REPO_DIR = os.path.join(HOMEPATH, '/home/riley/CY0420')



# replace with your homepath if you wanna test

# assert REPO_DIR == '/Users/cchilders/projects/trilogy_TA_class/lesson-plans/01-Class-Content'



def possibly_rename_repo(root, current_dir_name, target_dir_name):

    """

    Some were nested, could not automate:

        We would be renaming: /blah/blah/19.4/Activities/02-Class-Components-With-Props/Unsolved/Unsolved-Easier

    """

    fullpath =  os.path.join(root, current_dir_name)

    print("\n\n\nFile %s\n" % (bcolors.OKBLUE + fullpath + bcolors.ENDC))



    # if the folder is nested, like .../02-Class-Components-With-Props/Unsolved/Unsolved-Easier

    if fullpath.lower().count('solved') > 1:

        response = input("Hit enter to prune, \n's' to skip, \nor enter a custom name to rename custom\n")



        if response == 's':

            return



        elif not response:

            replacements = ['UNSOLVED', 'Unsolved', 'unsolved', 'SOLVED', 'Solved', 'solved', '-']

            target_dir_name = current_dir_name

            for item in replacements:

                target_dir_name = target_dir_name.replace(item, '')



        elif response:

            # overwrite the 'SOLVED' or 'UNSOLVED' option with a custom name

            target_dir_name = response



    target_path = os.path.join(root, target_dir_name)

    os.rename(fullpath, target_path)



    print("Renamed\n")

    print(bcolors.HEADER + fullpath + bcolors.ENDC)

    print("  to")

    print(bcolors.WARNING + target_path + bcolors.ENDC)





for root, dirs, files in os.walk(REPO_DIR):

    for this_dir in dirs:



        fullpath = os.path.join(root, this_dir)



        if 'solved' in this_dir.lower() and not 'unsolved' in this_dir.lower():

            if not this_dir == 'SOLVED':

                # print("We would be renaming: %s" % fullpath)

                possibly_rename_repo(root, this_dir, 'SOLVED')



        elif 'unsolved' in this_dir.lower():

            if not this_dir == 'UNSOLVED':

                # print("We would be renaming: %s" % fullpath)

                possibly_rename_repo(root, this_dir, 'UNSOLVED')



        else:

            pass