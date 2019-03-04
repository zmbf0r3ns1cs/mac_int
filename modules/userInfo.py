# Query Logic for User Information v0.3
# Justin Boncaldo, Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re
from var_db import *


# Specify files here for testing
#file = open('/Users/zachburnham/Desktop/Capstone/Mac_apt_Output/exampleWrite.txt', 'w+')
#connection = sqlite3.connect('/Users/zachburnham/Desktop/Capstone/Mac_apt_Output/mac_apt02.db')
file = open('E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\exampleWrite.txt', 'w+')
connection = sqlite3.connect('E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\mac_apt02.db')


cursor = connection.cursor()

# Mounted Volume variables
global a, b, c, g, h, i, output

def userInfoRun():
    global a, b, c, g, h, i, output
    # Define strings
    d = []
    e = []
    # Define counters
    end = "no"
    counter = 0
    output = None

    userSearch = input("What User? (Enter for default All): ")
    print("Starting Parsing for  " + str(userSearch) + "...")
    while end != "yes":
        # These require two parameters
        # Round 1 includes InstallHistory and NetUsage. Only require one parameter
        # 0 - 2 = InstallHistory
        # 3 - 9 = NetUsage
        # Round 2 includes RecentItems, Safari. Require two parameters (Add BashSessions and Quarantine)
        # 10 - 11 = RecentItems
        # 14 - 17 = DockItems
        # 16 - 17 = Safari
        # Round 3 includes Users and Spotlight
        # 18 - 20 Quarantine
        if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            print("[~] Finding Updates...")
            while counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                if counter == 0:
                    a = dN
                    b = ih
                    c = pN
                    g = macOS
                elif counter == 1:
                    a = dN
                    b = ih
                    c = pN
                    g = softwareupdated
                elif counter == 2:
                    a = dN
                    b = ih
                    c = pN
                    g = installer
                elif counter == 3:
                    a = n
                    b = nU
                    c = T
                    g = App
                elif counter == 4:
                    a = fSD
                    b = nU
                    c = T
                    g = App
                elif counter == 5:
                    a = lSD
                    b = nU
                    c = T
                    g = App
                elif counter == 6:
                    a = win
                    b = nU
                    c = T
                    g = App
                elif counter == 7:
                    a = wout
                    b = nU
                    c = T
                    g = App
                elif counter == 8:
                    a = wirIn
                    b = nU
                    c = T
                    g = App
                elif counter == 9:
                    a = wirOut
                    b = nU
                    c = T
                    g = App
                else:
                    print("A counting error has occurred")

                cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c), (g,))
                output = cursor.fetchall()
                d.clear()
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    # Volume Name List Start
                    if counter == 0:
                        user_processName1List.append(string1)
                        user_pNLength1: int = len(user_processName1List)
                    elif counter == 1:
                        user_processName2List.append(string1)
                        user_pNLength2: int = len(user_processName2List)
                    elif counter == 2:
                        user_processName3List.append(string1)
                        user_pNLength3: int = len(user_processName3List)
                    elif counter == 3:
                        user_appName_List.append(string1)
                        user_AppNameLength: int = len(user_appName_List)
                    elif counter == 4:
                        user_fSD_List.append(string1)
                        user_fSDLength: int = len(user_fSD_List)
                    elif counter == 5:
                        user_lSD_List.append(string1)
                        user_lSDLength: int = len(user_lSD_List)
                    elif counter == 6:
                        user_wifiIn_List.append(string1)
                        user_wifiInLength: int = len(user_wifiIn_List)
                    elif counter == 7:
                        user_wifiOut_List.append(string1)
                        user_wOutLength: int = len(user_wifiOut_List)
                    elif counter == 8:
                        user_wiredIn_List.append(string1)
                        user_wirInLength: int = len(user_wiredIn_List)
                    elif counter == 9:
                        user_wiredOut_List.append(string1)
                        user_wirOutLength: int = len(user_wiredOut_List)

                    else:
                        continue
                counter = counter + 1

        elif counter in (10, 11, 12, 13, 14, 15, 16, 17):
            print("[~] Finding User Downloads...")
            while counter in (10, 11, 12, 13, 14, 15, 16, 17):
                if counter == 10:
                    a = n
                    b = ri
                    c = T
                    g = u
                    h = application
                    i = userSearch
                elif counter == 11:
                    a = url
                    b = ri
                    c = T
                    g = u
                    h = application
                    i = userSearch
                elif counter == 12:
                    a = NoT
                    b = S
                    c = T
                    g = u
                    h = dL
                    i = userSearch
                elif counter == 13:
                    a = url
                    b = S
                    c = T
                    g = u
                    h = dL
                    i = userSearch
                elif counter == 14:
                    a = fL
                    b = di
                    c = u
                    g = fT
                    h = userSearch
                    i = appCode
                elif counter == 15:
                    a = pM
                    b = di
                    c = u
                    g = fT
                    h = userSearch
                    i = appCode
                elif counter == 16:
                    a = fM
                    b = di
                    c = u
                    g = fT
                    h = userSearch
                    i = appCode
                elif counter == 17:
                    a = fP
                    b = di
                    c = u
                    g = fT
                    h = userSearch
                    i = appCode
                else:
                    print("A counting error has occurred")

                cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
                output = cursor.fetchall()
                d.clear()
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    # Volume Name List Start
                    if counter == 10:
                        user_recentIName_List.append(string1)
                        user_riNLength1: int = len(user_recentIName_List)
                    elif counter == 11:
                        user_recentIURL_List.append(string1)
                        riURLLength1: int = len(user_recentIURL_List)
                    elif counter == 12:
                        user_SNoT_List.append(string1)
                        sNoTLength1: int = len(user_SNoT_List)
                    elif counter == 13:
                        user_sURL_List.append(string1)
                        sURLLength1: int = len(user_sURL_List)
                    elif counter == 14:
                        user_fileLabelList.append(string1)
                        fLLength: int = len(user_fileLabelList)
                    elif counter == 15:
                        user_parentModifiedList.append(string1)
                        pMLength: int = len(user_parentModifiedList)
                    elif counter == 16:
                        user_fileModifiedList.append(string1)
                        fMLength: int = len(user_fileModifiedList)
                    elif counter == 17:
                        user_filePathList.append(string1)
                        fPLength: int = len(user_filePathList)
                    else:
                        continue
                counter = counter + 1

        # Spotlight database for individual has to reference Users first for UID
        elif counter == 18:
            # Need to find user's UID first from Users table
            cursor.execute('SELECT UID FROM Users WHERE Username=?', (userSearch,))
            output = cursor.fetchall()
            d.clear()
            for row in output:
                d.append(str(row[0]))
            pos = 0
            for (row) in output:
                string1 = str(d[pos])
                pos = pos + 1
                user_userUID_List.append(string1)  # This now holds the user's UID
            counter = counter + 1

        # Starts actual spotlight parsing now
        elif counter in (19, 20, 21, 22, 23, 24):
            print("[~] Finding User's Applications...")
            while counter in (19, 20, 21, 22, 23, 24):
                if counter == 19:  # Starts checks for pue in everything. Then needs to check for com.microsoft
                    a = idn
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = pue
                elif counter == 20:
                    a = ifn
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = pue
                elif counter == 21:
                    a = ik
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = pue
                elif counter == 22:
                    a = ps
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = pue
                elif counter == 23:
                    a = ida
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = pue
                elif counter == 24:
                    a = iwf
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = pue
                else:
                    print("A counting error has occurred")
                cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
                output = cursor.fetchall()
                d.clear()
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    if counter == 19:
                        user_idn_List.append(string1)  # This now holds the user's UID
                    elif counter == 20:
                        user_ifn_List.append(string1)
                    elif counter == 21:
                        user_ik_List.append(string1)
                    elif counter == 22:
                        user_ps_List.append(string1)
                    elif counter == 23:
                        user_ida_List.append(string1)
                    elif counter == 24:
                        user_iwf_List.append(string1)
                    else:
                        continue
                counter = counter + 1

        # Continues spotlight parsing now
        elif counter in (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36):
            while counter in (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36):
                if counter == 25:  # Starts checks for com.microsoft
                    a = idn
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = cmwe
                elif counter == 26:
                    a = ifn
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = cmwe
                elif counter == 27:
                    a = ik
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = cmwe
                elif counter == 28:
                    a = ps
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = cmwe
                elif counter == 29:
                    a = ida
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = pue
                elif counter == 30:
                    a = iwf
                    b = sls
                    c = ioUID
                    g = ict
                    h = str(user_userUID_List[0])
                    i = cmwe
                elif counter == 31:  # RecentItems for VOLUMES
                    a = n
                    b = ri
                    c = T
                    g = u
                    h = volume
                    i = userSearch
                elif counter == 32:
                    a = url
                    b = ri
                    c = T
                    g = u
                    h = volume
                    i = userSearch
                elif counter == 33:
                    a = "Info"
                    b = ri
                    c = T
                    g = u
                    h = volume
                    i = userSearch
                elif counter == 34:  # RecentItems for PLACE
                    a = n
                    b = ri
                    c = T
                    g = u
                    h = place
                    i = userSearch
                elif counter == 35:
                    a = url
                    b = ri
                    c = T
                    g = u
                    h = place
                    i = userSearch
                elif counter == 36:
                    a = "Info"
                    b = ri
                    c = T
                    g = u
                    h = place
                    i = userSearch

                else:
                    print("A counting error has occurred")
                cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i,))
                output = cursor.fetchall()
                d.clear()
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    if counter == 25:
                        user_idn2_List.append(string1)
                        idn2Length = len(user_idn2_List)
                    elif counter == 26:
                        user_ifn2_List.append(string1)
                    elif counter == 27:
                        user_ik2_List.append(string1)
                    elif counter == 28:
                        user_ps2_List.append(string1)
                    elif counter == 29:
                        user_ida2_List.append(string1)
                    elif counter == 30:
                        user_iwf2_List.append(string1)
                    elif counter == 31:
                        user_riNamevol_List.append(string1)
                    elif counter == 32:
                        user_riURLvol_List.append(string1)
                    elif counter == 33:
                        user_riInfovol_List.append(string1)
                    elif counter == 34:
                        user_riNameplace_List.append(string1)
                    elif counter == 35:
                        user_riURLplace_List.append(string1)
                    elif counter == 36:
                        user_riInfoplace_List.append(string1)
                    else:
                        continue
                counter = counter + 1

        elif counter in (37, 38, 39):
            while counter in (37, 38, 39):
                if counter == 37:
                    a = date
                    b = ih
                    c = pN
                    g = macOS
                elif counter == 38:
                    a = date
                    b = ih
                    c = pN
                    g = softwareupdated
                elif counter == 39:
                    a = date
                    b = ih
                    c = pN
                    g = installer
                else:
                    print("A counting error has occurred")
                cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c), (g,))
                output = cursor.fetchall()
                d.clear()
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    # Volume Name List Start
                    if counter == 37:
                        user_date1List.append(string1)
                        user_pNLength1: int = len(user_date1List)
                    elif counter == 38:
                        user_date2List.append(string1)
                        user_pNLength2: int = len(user_date2List)
                    elif counter == 39:
                        user_date3List.append(string1)
                        user_pNLength3: int = len(user_date3List)
                    else:
                        continue
                counter = counter + 1
        else:
            end = "yes"

            # Recent Applications Write
            line1 = 0
            writePos1 = 0
            if line1 != len(user_recentIName_List):
                file.write(str(userSearch) + " has recently used these applications:\n")
            else:
                file.write(str(userSearch) + " has no recently used applications\n")
            while line1 < len(user_recentIName_List):
                file.write(
                    "\t•'" + str(user_recentIName_List[writePos1]) + "' from the location '" + str(
                        user_recentIURL_List[writePos1]) + "'\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Recent Volumes Write
            line1 = 0
            writePos1 = 0
            if line1 != len(user_riNamevol_List):
                file.write(str(userSearch) + " has recently interacted with these volumes:\n")
            else:
                file.write(str(userSearch) + " has not recently interacted with any volumes\n")
            while line1 < len(user_riNamevol_List):
                file.write(
                    "\t•'" + str(user_riNamevol_List[writePos1]) + "' from the location '" + str(
                        user_riURLvol_List[writePos1]) + "' on " + str(user_riInfovol_List[writePos1]) + "\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Recent Places Write
            line1 = 0
            writePos1 = 0
            if line1 != len(user_riNameplace_List):
                file.write(str(userSearch) + " has recently visited these places:\n")
            else:
                file.write(str(userSearch) + " has no folder activity\n")
            while line1 < len(user_riNameplace_List):
                file.write(
                    "\t•'" + str(user_riNameplace_List[writePos1]) + "' from the location '" + str(
                        user_riURLplace_List[writePos1]) + "\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Shows the user's downloads from Safari
            line1 = 0
            writePos1 = 0
            if line1 != len(user_SNoT_List):
                file.write(str(userSearch) + " has downloaded the following files from Safari:\n")
            else:
                file.write(str(userSearch) + " has no Safari Downloads\n")
            while line1 < len(user_SNoT_List):
                file.write(
                    "\t•'" + str(user_SNoT_List[writePos1]) + "' from the url '" + str(
                        user_sURL_List[writePos1]) + "'\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Shows user's Unix Executables
            line1 = 0
            writePos1 = 0
            if line1 != len(user_idn_List):
                file.write(" These are " + str(userSearch) + "'s Unix Executables:\n")
            else:
                file.write(str(userSearch) + " has no Unix executables\n")
            while line1 < len(user_idn_List):
                file.write(
                    "\t•'" + str(user_idn_List[writePos1]) + "'\n" + "\t\tItem File Name: " + str(
                        user_ifn_List[writePos1]) + "\n" + "\t\tItem Kind: " + str(
                        user_ik_List[writePos1]) + "\n" + "\t\tPhysical Size: " + str(
                        user_ps_List[writePos1]) + " bytes\n" + "\t\tDate it was added to this system: " + str(
                        user_ida_List[writePos1]) + "\n" + "\t\tWhere it came from: " + str(
                        user_iwf_List[writePos1]) + "\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Shows user's Microsoft Windows Executables
            line1 = 0
            writePos1 = 0
            if line1 != len(user_idn_List):
                file.write(" These are " + str(userSearch) + "'s Microsoft Windows Executables:\n")
            else:
                file.write(str(userSearch) + " has no Microsoft Windows Executables\n")
            while line1 < len(user_idn2_List):
                file.write("\t•'" + str(user_idn2_List[writePos1]) + "'\n" + "\t\tItem File Name: " + str(
                    user_ifn2_List[writePos1]) + "\n" + "\t\tItem Kind: " + str(
                    user_ik2_List[writePos1]) + "\n" + "\t\tPhysical Size: " + str(
                    user_ps2_List[writePos1]) + " bytes\n" + "\t\tDate it was added to this system: " + str(
                    user_ida2_List[writePos1]) + "\n" + "\t\tWhere it came from: " + str(
                    user_iwf2_List[writePos1]) + "\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Run Bash Session connections
            # SQLite Search for Session Start
            a = ss
            b = bs
            cursor.execute('SELECT "{}" FROM "{}" WHERE User = ?'.format(a, b), (userSearch,))
            bashOutput = cursor.fetchall()
            del e[:]
            for i in bashOutput:
                e.append(str(i[0]))
                pos = 0
                string1 = str(i[pos])
                pos = pos + 1
                user_bashSSList.append(string1)
            a = se
            b = bs
            cursor.execute('SELECT "{}" FROM "{}" WHERE User = ?'.format(a, b), (userSearch,))
            bashOutput = cursor.fetchall()
            del e[:]
            for i in bashOutput:
                e.append(str(i[0]))
                pos = 0
                string1 = str(i[pos])
                pos = pos + 1
                user_bashSEList.append(string1)
            a = sc
            b = bs
            cursor.execute('SELECT "{}" FROM "{}" WHERE User = ?'.format(a, b), (userSearch,))
            bashOutput = cursor.fetchall()
            del e[:]
            for i in bashOutput:
                e.append(str(i[0]))
                pos = 0
                string1 = str(i[pos])
                pos = pos + 1
                user_bashSCList.append(string1)

            # Bash Writing
            bashWriteCounter = 0
            L = 0
            bashSess = 1
            if line1 != len(user_bashSSList):
                file.write("These are " + str(userSearch) + "'s bash sessions:\n")
            else:
                file.write(str(userSearch) + " has no bash sessions\n")

            while bashWriteCounter < len(user_bashSSList):
                file.write("\t\tSession " + str(bashSess) + "\n")
                file.write("\t\tSession Start: " + str(user_bashSSList[L]) + "\n\t\tSession End: " + str(
                    user_bashSEList[L]) + "\n\t\tSession Commands: \n\t\t" + str(user_bashSCList[L]) + "\n")
                L = L + 1
                bashWriteCounter = bashWriteCounter + 1
                bashSess = bashSess + 1


userInfoRun()


# Global Variables
a = "None"
b = "None"
c = "None"
g = "None"
h = "None"
i = "None"
output = None

# End Parsing
print("Installed Application Parsing Completed!")
