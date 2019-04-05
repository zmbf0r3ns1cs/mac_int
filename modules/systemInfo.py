# Query Logic for System Information v1.0
# Justin Boncaldo (@boncaldoj), Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re
from var_db import *

# Start of function called upon by Main Function (mac_int.py)
def systemInfoRun(output_dir, input_path, user_name):
    # Output file and DB specified in mac_int.py
    file = open(output_dir + "\\mac_int-SYSTEMINFO-" + user_name + "-Output.txt", 'w+')
    connection = sqlite3.connect(input_path)
    cursor = connection.cursor()

    # Define Global variables
    global a, b, c, g, h, i, output, userSearch

    # Username search (determined in mac_int.py)
    userSearch = user_name

    def systemInfo():
        #global a, b, c, g, h, i, output, userSearch
        # Define strings
        d = []
        e = []
        # Define counters
        end = "no"
        counter = 0
        output = None

        print("[#] Parsing System Information...")
        while end != "yes":
            if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18):
                print("[~] Grabbing Model and macOS Version...")
                while counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18):
                    if counter == 0:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Model"
                    elif counter == 1:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "OSX Version"
                    elif counter == 2:
                        print("[~] Grabbing Serial Number...")
                        a = 'Description'
                        b = bI
                        c = n
                        g = "OSX Version"
                    elif counter == 3:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Mac Serial Number"
                    elif counter == 4:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "ComputerName"
                    elif counter == 5:
                        print("[~] Grabbing Hostname...")
                        a = 'Data'
                        b = bI
                        c = n
                        g = "LocalHostName"
                    elif counter == 6:
                        print("[~] Grabbing Timezone...")
                        a = 'Data'
                        b = bI
                        c = n
                        g = "TimeZone Set"
                    elif counter == 7:
                        print("[~] Grabbing Last User Logon...")
                        a = 'Data'
                        b = bI
                        c = n
                        g = "lastUserName"
                    elif counter == 8:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "lastUser"
                    elif counter == 9:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "lastLoginPanic"
                    elif counter == 10:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "LoginwindowText"
                    elif counter == 11:
                        print("[~] Grabbing File System Metadata...")
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Number of Files"
                    elif counter == 12:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Number of Folders"
                    elif counter == 13:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Block Size"
                    elif counter == 14:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Created date"
                    elif counter == 15:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Last Modified date"
                    elif counter == 16:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Last Checked date"
                    elif counter == 17:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Last Backup date"
                    elif counter == 18:
                        a = 'Data'
                        b = bI
                        c = n
                        g = "Last Mounted Version"
                    else:
                        print("A counting error has occurred")

                    cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c), (g,))
                    output = cursor.fetchall()

                    del d[:]
                    for row in output:
                        d.append(str(row[0]))
                    pos = 0
                    for (row) in output:
                        string1 = str(d[pos])
                        pos = pos + 1
                        # Volume Name List Start
                        if counter == 0:
                            print("[~] Grabbing Volume Metadata...")
                            system_Model = string1
                        elif counter == 1:
                            system_version1 = string1
                        elif counter == 2:
                            system_version2 = string1
                        elif counter == 3:
                            system_serial = string1
                        elif counter == 4:
                            #print("[~] 60%...")
                            system_computerName = string1
                        elif counter == 5:
                            system_localHostName = string1
                        elif counter == 6:
                            system_timezone = string1
                        elif counter == 7:
                            system_lastUserName = string1
                        elif counter == 8:
                            system_lastLoginStatus = string1
                        elif counter == 9:
                            system_lastLoginTime = string1
                        elif counter == 10:
                            #print("[~] 70%...")
                            system_loginText = string1
                        elif counter == 11:
                            system_NumberofFiles = string1
                        elif counter == 12:
                            system_NumberofFolders = string1
                        elif counter == 13:
                            system_blockSize = string1
                        elif counter == 14:
                            system_Created = string1
                        elif counter == 15:
                            #print("[~] 80%...")
                            system_Modified = string1
                        elif counter == 16:
                            system_Checked = string1
                        elif counter == 17:
                            system_Backup = string1
                        elif counter == 18:
                            #print("[~] 90%...")
                            system_Mounted = string1
                        else:
                            continue
                    counter = counter + 1

            else:
                end = "yes"

                # Recent Applications Write
                file.write("Model Name: " + str(system_Model) + "\nOSX Version: " + str(
                    system_version2) + " " + str(system_version1) + "\nHardware Serial Number: " + str(
                    system_serial) + "\n\nComputer Name: " + str(system_computerName) + "\nLocal Host Name: " + str(
                    system_localHostName) + "\nMac's Timezone: " + str(
                    system_timezone) + "\n\nLast User: " + str(system_lastUserName) + "\nLast User Status: " + str(
                    system_lastLoginStatus) + "\nLast Login Time: " + str(
                    system_lastLoginTime) + "\nMac Login Window Text: " + str(
                    system_loginText) + "\n\nVolume's Total Files: " + str(system_NumberofFiles) + "\nVolume's Total Folders: " + str(
                    system_NumberofFolders) + "\nVolume's Block Size: " + str(
                    system_blockSize) + "\nVolume Created Date: " + str(
                    system_Created) + "\nVolume's Last Modified Date: " + str(
                    system_Modified) + "\nLast Time Volume Check for Errors: " + str(
                    system_Checked) + "\nLast Time Volume Backed Up: " + str(
                    system_Backup) + "\nLast Volume Mount version: " + str(
                    system_Mounted))

                file.write("\n\n")

    # Global Variables
    a = "None"
    b = "None"
    c = "None"
    g = "None"
    h = "None"
    i = "None"
    output = None
    userSearch = None

    ############# MAIN FUNCTION #############

    # Run Functions
    systemInfo()

    # Show When Parsing Completed
    #print("[~] 100%...")
    print("[*] System Information Parsing Completed!")