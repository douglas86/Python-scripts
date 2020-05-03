#!/usr/bin/python3

#  modules that are importing
from os import system
import time
import datetime

#  Starting time and date
start_time = time.time() # starting time in seconds
date = datetime.date.today().strftime("%d-%m-%Y") 
current_time = time.strftime("%H:%M:%S") 
now = "Date: " + date + " " + "Time: " + current_time

#  calculates the time taken
def end_of_time():
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

#  spacing between different sections
def spacing():
    print("")
    print("--------------------------------------------------")
    print("")

#  lists for what to backup and times for each item
backups = [
        "Documents", 
        "Pictures", 
        "Dropbox",
        "Programming", 
        "Videos", 
        ".vim", 
        ".vscode", 
        ".vimrc",
        ]

times = []

#  starting time and current date
print("Start date and time: ")
print(now)

#  converting seconds to hours min and seconds format
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return("{}h {}m {}s".format(int(hours),int(mins),round(sec, 5)))

#  calculates final time taken
def end_of_time(started):
    end_time = time.time()
    time_lapsed = end_time - started
    return time_convert(time_lapsed)

def prCyan(skk, backups): 
    print("\033[96m{} {}\033[00m".format(skk, backups))

#  rsync backuping up
for item in range(len(backups)):
    spacing()
    started = time.time()
    #  print("Backing up " + str(backups[item]))
    prCyan("Backup up ", str(backups[item]))
    system("rsync -avPzh ~/" + str(backups[item]) + " ~/Insync/'Local Backups' --delete --exclude 'node_modules'")
    print("This script took: " + end_of_time(started))
    times.append(end_of_time(started))

spacing()
print("Time to complete script: " + end_of_time(start_time))

#  prints the final time and date
print(now)

#  opening the txt file to write to
file_object = open("/home/douglas/Documents/Documents/Text documents/Backup_logs.txt", 'a')

#  writing to the txt file
file_object.write("\n")
file_object.write("\n" + str(now))
for i in range(len(backups)):
    file_object.write("\n" + backups[i] + " took: " + str(times[i]))
file_object.write("\nTotal time of script: " + str(end_of_time(start_time)))

#  closing the txt file after writing to it
file_object.close()
