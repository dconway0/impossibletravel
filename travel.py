# Simple program to read input file of authentication logs to detect impossible travel
import sys
import csv
from datetime import datetime

if (len(sys.argv) < 2 ) or (len(sys.argv) > 3):
    exit("To run: python3 travel.py [input csv file] [1 (default) or 2]")

file = sys.argv[1]

if file[-4:] != '.csv':
    exit("Input file must be .csv")

choice = 1
if len(sys.argv) == 3:
    try:
        arg = int(sys.argv[2])
        if arg in (1, 2):
            choice = arg
        else:
            exit("Second argument should be 1 or 2. Default is 1.")
    except ValueError:
        exit("Second argumet should be int, 1 or 2. Default is 1.")

#open csv, make into list of dicts, sort by timestamp
with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    data = [row for row in reader]

    sorted_data = sorted(data, key=lambda row: datetime.strptime(row['timestamp'], "%Y-%m-%dT%H:%M:%SZ"))

#make list of unique usernames
uniqueUsers = []
for row in sorted_data:
    if row['username'] not in uniqueUsers:
        uniqueUsers.append(row['username'])
if choice == 1:
#make dictionary where each unique username will map to one row of theirs
    currUserLogs = {user: [] for user in uniqueUsers}
    f = open("first.txt", "w")

    logCount = 0

    for log in sorted_data:
    #if a username has no value yet, make the matched log the value. So we have a dict where a username key maps to one row (which is itself a dict)
        if currUserLogs[log['username']] == []:
            currUserLogs[log['username']] = log
    #if otherwise, this means we have found a new log with a username that already has a previous row found
        else:
        #if the locations of the logs do not match, impossible travel. Make newly found row the value for the username. In future, will make impossible travel check more in depth
            if currUserLogs[log['username']]['location'] != log['location']:
            #print("impossible travel") write log info to unique output file and check equivalence with ai
                f.write(f'{log['username']}: {currUserLogs[log['username']]['location']} to {log['location']}\n')
                logCount += 1
                currUserLogs[log['username']] = log

    print(logCount)
    f.close()

if choice == 2:
    f = open("second.txt", "w")
    completedUsers = []
    logCount = 0
    rowPlace = 0
    for row in sorted_data:
        if row['username'] not in completedUsers:
            currLog = row
            nextPlace = rowPlace
            while nextPlace < len(sorted_data):
                if currLog['username'] == sorted_data[nextPlace]['username'] and currLog['location'] != sorted_data[nextPlace]['location']:
                    f.write(f'{currLog['username']}: {currLog['location']} to {sorted_data[nextPlace]['location']}\n')
                    logCount += 1
                    currLog = sorted_data[nextPlace]
                nextPlace += 1
            completedUsers.append(currLog['username'])
            if set(completedUsers) == set(uniqueUsers):
                break
        rowPlace += 1
    print(logCount)
    f.close()        

