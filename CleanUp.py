import os
import time

DAYS = 5              # Maximal age of file to stay, older will be deleted
FOLDERS = [
           "\home\ubuntu\/trash",                         # For Windows, the path should look like C:\Users\user\Downloads\"
           "\/var\log\someoneLogDir"
]
TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0


nowTime = time.time()                                     # Get current time in seconds
ageTime = nowTime - 60*60*24*DAYS                         # Minus days in seconds

def delete_old_files(folder):
    """Delete files older than x days"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)           # Get full path to file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile            # Count sum of all free space
                TOTAL_DELETED_FILE += 1                   #Count number of deleted files
                print("Deleting file: " + str(fileName))
                os.remove(fileName)                       # Delete file

def delete_empty_dir(foldet):
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_run += 1
            print ("Deleting empty Dir " + str(path))
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_dir(folder)

#===========MAIN=============
starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_dir(folder)


finishtime = time.asctime()


print("=========================================================")
print("Start time: "                  + str(starttime))
print("Total deleted size: "          + str(TOTAL_DELETED_SIZE/1024/1024) + "MB")
print("Total deleted files: "         + str(TOTAL_DELETED_FILE))
print("Total deleted empty folders: " + str(TOTAL_DELETED_DIRS))
print("Finish time: "                 + str(finishtime))
print("=========================================================")