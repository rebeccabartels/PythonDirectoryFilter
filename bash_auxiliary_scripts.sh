#copying a source to a dest 
cp -r /source/ /dest 
cp -r /home/riley/Dev/CyberSecTA/LessonPlans/cybersecurity-v2/ /home/riley/CY0420



#find <search directory> <search pattern> <action>
find . -name \*.png
#find x in  directory type files not case sensitive 
find /home/riley/CU0420GitLab/ -type f -iname "lessonplan.md"
#Output: 
#/home/riley/CU0420GitLab/01-Cybersecurity-101/2/LessonPlan.md
#/home/riley/CU0420GitLab/01-Cybersecurity-101/3/LessonPlan.md
#/home/riley/CU0420GitLab/01-Cybersecurity-101/1/LessonPlan.md


# the above find command plus removing the output files 
find /home/riley/CU0420GitLab/ -type f -iname "lessonplan.md" -exec rm -f {} \;

#find all pics in dir from home directory (cd)
find /home/riley/CU0420GitLab/01-Cybersecurity-101/ -type f -iname "*.png"  


#rsync exclusion multiple times 
rsync -av --progress /home/riley/CY0420/1-Lesson-Plans/02-GRC /home/riley/CU0420GitLab --exclude SOLVED



#rsync 
rsync -av --exclude-from=SOLVED /home/riley/CY0420/1-Lesson-Plans/02-GRC/*/SOLVED/* /home/riley/CU0420GitLab


#Source 
/home/riley/CY0420/1-Lesson-Plans/02-GRC

#dest
/home/riley/CU0420GitLab


tar -zcvf /home/riley/CU0420GitLab.tar.gz --exclude "SOLVED" /home/riley/CY0420/1-Lesson-Plans 


#extract tar.gz
tar -xf archive.tar.gz


#exclode all folders with name "x"
find ./servers -type -d -name *log* > excludefiles

# ****SOLVED -> Script to Filter Out "Solved" Asignments from Github Directory 
find ./CY0420  -iwholename */solved* > excludefiles

find ./CY0420  -iwholename */lessonplan.md* > excludefiles01


# combining several txt files into one 
cat file1 file2 file3 > newfile

#add files to existing doc
 cat file1 file2 file3 >> destfile

find ./CY0420  -iwholename */.contributing.md* > excludefiles012
# aksi did .gitattributes 


#filtering tar file with the filterfile 
tar czf /home/riley/CY0420/.tar.gz -X filteredData01.txt ./CY0420/


#search for text in file 


grep -iRl "tar" ./


# find one down in directory all directories 
find . -mindepth 1 -type d
