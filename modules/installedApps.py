# Query Logic for Installed Applications v1.0
# Justin Boncaldo (@boncaldoj), Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re
from var_db import *

# Start of function called upon by Main Function (mac_int.py)
def installedAppsRun(output_dir, input_path, user_name):
    connection = sqlite3.connect(input_path)
    cursor = connection.cursor()

    # Mounted Volume variables
    global a, b, c, g, h, i, output, nonUserSpecific

    def generalSystem():
        global a, b, c, g, h, i, output
        # Define strings
        d = []

        # Define counters
        endGen = "no"
        counter = 0
        output = None

        # Define variables for table
        while endGen != "yes":

            # Round 1 includes InstallHistory, DockItems, and NetUsage. Only require one parameter
            # 0 - 2 = InstallHistory
            # 3 - 9 = NetUsage
            # 10 - 12 = InstallHistory


            if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
                print("[~] Finding General Software and Application Information...")
                while counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
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
                    elif counter == 10:
                        a = date
                        b = ih
                        c = pN
                        g = macOS
                    elif counter == 11:
                        a = date
                        b = ih
                        c = pN
                        g = softwareupdated
                    elif counter == 12:
                        a = date
                        b = ih
                        c = pN
                        g = installer
                    else:
                        print("[!] A counting error has occurred")

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
                            inst_processName1List.append(string1)
                            pNLength1 = int = len(inst_processName1List)
                        elif counter == 1:
                            inst_processName2List.append(string1)
                            pNLength2 = int = len(inst_processName2List)
                        elif counter == 2:
                            inst_processName3List.append(string1)
                            pNLength3 = int = len(inst_processName3List)
                        elif counter == 3:
                            inst_appName_List.append(string1)
                            AppNameLength = int = len(inst_appName_List)
                        elif counter == 4:
                            inst_fSD_List.append(string1)
                            fSDLength = int = len(inst_fSD_List)
                        elif counter == 5:
                            inst_lSD_List.append(string1)
                            lSDLength = int = len(inst_lSD_List)
                        elif counter == 6:
                            inst_wifiIn_List.append(string1)
                            AppNameLength = int = len(inst_wifiIn_List)
                        elif counter == 7:
                            inst_wifiOut_List.append(string1)
                            wOutLength = int = len(inst_wifiOut_List)
                        elif counter == 8:
                            inst_wiredIn_List.append(string1)
                            wirInLength = int = len(inst_wiredIn_List)
                        elif counter == 9:
                            inst_wiredOut_List.append(string1)
                            wirOutLength = int = len(inst_wiredOut_List)
                        elif counter == 10:
                            inst_date1List.append(string1)
                            pNdateLength1 = int = len(inst_date1List)
                        elif counter == 11:
                            inst_date2List.append(string1)
                            pNdateLength2 = int = len(inst_date2List)
                        elif counter == 12:
                            inst_date3List.append(string1)
                            pNdateLength3 = int = len(inst_date3List)
                        else:
                            continue
                    counter = counter + 1

            else:
                # Calculates total app internet usage.
                # Steps through each app name, and adds up all wifi in/out and wired in/outs
                totalCount = 0
                posx = 0
                while totalCount < AppNameLength:
                    # Position of each item in lists
                    inst_totalNetUsage_List.append((float(inst_wifiIn_List[posx])) + float(inst_wifiOut_List[posx]) + float(inst_wiredIn_List[posx]) + float(inst_wiredOut_List[posx]))
                    totalCount = totalCount + 1
                    posx = posx + 1
                endGen = "yes"

        # Writing non-specfic findings out -----------------------------

        #Writing out different installer types (macOS, software update, installers)
        line1 = 0
        writePos1 = 0
        file.write("[*] The following outputs are non-user specific, until specified\n\n")
        file.write("There was a macOS update instance performed on this system by:\n")
        while line1 < pNLength1:
            file.write("\t-'" + str(inst_processName1List[writePos1]) + "' on " + str(inst_date1List[writePos1]) + "\n")
            line1 = line1 + 1
            writePos1 = writePos1 + 1
        file.write("\n\n")

        line1 = 0
        writePos1 = 0
        file.write("The following software updaters were seen running on this system:\n")
        while line1 < pNLength2:
            file.write("\t-'" + str(inst_processName2List[writePos1]) + "' on " + str(inst_date2List[writePos1]) + "\n")
            line1 = line1 + 1
            writePos1 = writePos1 + 1
        file.write("\n\n")

        line1 = 0
        writePos1 = 0
        file.write("The following application installers were run on this system:\n")
        while line1 < pNLength3:
            file.write("\t-'" + str(inst_processName3List[writePos1]) + "' on " + str(inst_date3List[writePos1]) + "\n")
            line1 = line1 + 1
            writePos1 = writePos1 + 1
        file.write("\n\n")

        # Writing file items for NetUsage -----------------------------
        line1 = 0
        writePos1 = 0
        file.write("Network usage was found for the following applications on this system:\n")
        while line1 < AppNameLength:
            file.write("\t-'" + str(inst_appName_List[writePos1]) + "' used a total of " + str(
                inst_totalNetUsage_List[writePos1]) + " bytes\n" + "\t\tFirst Seen on " + str(
                inst_fSD_List[writePos1]) + " and Last Seen on " + str(
                inst_lSD_List[writePos1]) + "\n\t\tWifi bytes in:\t " + str(inst_wifiIn_List[writePos1])
                    + "\n\t\tWifi bytes out:\t " + str(inst_wifiOut_List[writePos1]) + "\n\t\tWired bytes in:\t " + str(
                inst_wiredIn_List[writePos1]) + "\n\t\tWired bytes out: " + str(inst_wiredOut_List[writePos1]) + "\n")
            line1 = line1 + 1
            writePos1 = writePos1 + 1
        file.write("\n\n")




    def userSpecificSearch():
        global a, b, c, g, h, i, output
        # Define strings
        d = []
        # Define counters
        end = "no"
        counter = 0
        output = None

        userSearch = user_name
        print("[#] Starting Installed Application Parsing for " + str(userSearch) + "...")
        while end != "yes":
            # These require two parameters
            # Round 1 includes InstallHistory, DockItems, and NetUsage. Only require one parameter
            # 0 - 2 = InstallHistory
            # 3 - 9 = NetUsage
            # Round 2 includes RecentItems, Safari. Require two parameters (Add BashSessions and Quarantine)
            # 10 - 11 = RecentItems
            # 14 - 17 = DockItems
            # 16 - 17 = Safari
            # Round 3 includes Users and Spotlight
            # 18 - 20 Quarantine
            if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                print("[~] Finding any logged updates...")
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
                        print("[!] A counting error has occurred")

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
                            inst_processName1List.append(string1)
                            pNLength1 = int = len(inst_processName1List)
                        elif counter == 1:
                            inst_processName2List.append(string1)
                            pNLength2 = int = len(inst_processName2List)
                        elif counter == 2:
                            inst_processName3List.append(string1)
                            pNLength3 = int = len(inst_processName3List)
                        elif counter == 3:
                            inst_appName_List.append(string1)
                            AppNameLength = int = len(inst_appName_List)
                        elif counter == 4:
                            inst_fSD_List.append(string1)
                            fSDLength = int = len(inst_fSD_List)
                        elif counter == 5:
                            inst_lSD_List.append(string1)
                            lSDLength = int = len(inst_lSD_List)
                        elif counter == 6:
                            inst_wifiIn_List.append(string1)
                            AppNameLength = int = len(inst_wifiIn_List)
                        elif counter == 7:
                            inst_wifiOut_List.append(string1)
                            wOutLength = int = len(inst_wifiOut_List)
                        elif counter == 8:
                            inst_wiredIn_List.append(string1)
                            wirInLength = int = len(inst_wiredIn_List)
                        elif counter == 9:
                            inst_wiredOut_List.append(string1)
                            wirOutLength = int = len(inst_wiredOut_List)

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
                        print("[!] A counting error has occurred")

                    cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
                    output = cursor.fetchall()
                    del d[:]
                    for row in output:
                        d.append(str(row[0]))
                    pos = 0
                    for (row) in output:
                        string1 = str(d[pos])
                        pos = pos + 1
                        # Volume Name List Start
                        if counter == 10:
                            inst_recentIName_List.append(string1)
                            riNLength1 = int = len(inst_recentIName_List)
                        elif counter == 11:
                            inst_recentIURL_List.append(string1)
                            riURLLength1 = int = len(inst_recentIURL_List)
                        elif counter == 12:
                            inst_SNoT_List.append(string1)
                            sNoTLength1 = int = len(inst_SNoT_List)
                        elif counter == 13:
                            inst_sURL_List.append(string1)
                            sURLLength1 = int = len(inst_sURL_List)
                        elif counter == 14:
                            inst_fileLabelList.append(string1)
                            fLLength = int = len(inst_fileLabelList)
                        elif counter == 15:
                            inst_parentModifiedList.append(string1)
                            pMLength = int = len(inst_parentModifiedList)
                        elif counter == 16:
                            inst_fileModifiedList.append(string1)
                            fMLength = int = len(inst_fileModifiedList)
                        elif counter == 17:
                            inst_filePathList.append(string1)
                            fPLength = int = len(inst_filePathList)
                        else:
                            continue
                    counter = counter + 1

            # Spotlight database for individual has to reference Users first for UID
            elif counter == 18:
                # Need to find user's UID first from Users table
                cursor.execute('SELECT UID FROM Users WHERE Username=?', (userSearch,))
                output = cursor.fetchall()
                del d[:]
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    inst_userUID_List.append(string1)  # This now holds the user's UID
                counter = counter + 1

            # Starts actual spotlight parsing now
            elif counter in (19, 20, 21, 22, 23, 24):
                print("[~] Finding User Specific Applications...")
                while counter in (19, 20, 21, 22, 23, 24):
                    if counter == 19:  # Starts checks for pue in everything. Then needs to check for com.microsoft
                        a = idn
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = pue
                    elif counter == 20:
                        a = ifn
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = pue
                    elif counter == 21:
                        a = ik
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = pue
                    elif counter == 22:
                        a = ps
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = pue
                    elif counter == 23:
                        a = ida
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = pue
                    elif counter == 24:
                        a = iwf
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = pue
                    else:
                        print("[!] A counting error has occurred")
                    cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
                    output = cursor.fetchall()
                    del d[:]
                    for row in output:
                        d.append(str(row[0]))
                    pos = 0
                    for (row) in output:
                        string1 = str(d[pos])
                        pos = pos + 1
                        if counter == 19:
                            inst_idn_List.append(string1)  # This now holds the user's UID
                        elif counter == 20:
                            inst_ifn_List.append(string1)
                        elif counter == 21:
                            inst_ik_List.append(string1)
                        elif counter == 22:
                            inst_ps_List.append(string1)
                        elif counter == 23:
                            inst_ida_List.append(string1)
                        elif counter == 24:
                            inst_iwf_List.append(string1)
                        else:
                            continue
                    counter = counter + 1

            # Continues spotlight parsing now
            elif counter in (25, 26, 27, 28, 29, 30):
                while counter in (25, 26, 27, 28, 29, 30):
                    if counter == 25:  # Starts checks for com.microsoft
                        a = idn
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = cmwe
                    elif counter == 26:
                        a = ifn
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = cmwe
                    elif counter == 27:
                        a = ik
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = cmwe
                    elif counter == 28:
                        a = ps
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = cmwe
                    elif counter == 29:
                        a = ida
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = pue
                    elif counter == 30:
                        a = iwf
                        b = sls
                        c = ioUID
                        g = ict
                        h = str(inst_userUID_List[0])
                        i = cmwe
                    else:
                        print("A counting error has occurred")
                    cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
                    output = cursor.fetchall()
                    del d[:]
                    for row in output:
                        d.append(str(row[0]))
                    pos = 0
                    for (row) in output:
                        string1 = str(d[pos])
                        pos = pos + 1
                        if counter == 25:
                            inst_idn2_List.append(string1)
                            idn2Length = len(inst_idn2_List)
                        elif counter == 26:
                            inst_ifn2_List.append(string1)
                        elif counter == 27:
                            inst_ik2_List.append(string1)
                        elif counter == 28:
                            inst_ps2_List.append(string1)
                        elif counter == 29:
                            inst_ida2_List.append(string1)
                        elif counter == 30:
                            inst_iwf2_List.append(string1)
                        else:
                            continue
                    counter = counter + 1

            elif counter in (31, 32, 33):
                while counter in (31, 32, 33):
                    if counter == 31:
                        a = date
                        b = ih
                        c = pN
                        g = macOS
                    elif counter == 32:
                        a = date
                        b = ih
                        c = pN
                        g = softwareupdated
                    elif counter == 33:
                        a = date
                        b = ih
                        c = pN
                        g = installer
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
                        if counter == 31:
                            inst_date1List.append(string1)
                            pNLength1 = int = len(inst_date1List)
                        elif counter == 32:
                            inst_date2List.append(string1)
                            pNLength2 = int = len(inst_date2List)
                        elif counter == 33:
                            inst_date3List.append(string1)
                            pNLength3 = int = len(inst_date3List)
                        else:
                            continue
                    counter = counter + 1
            else:
                end = "yes"

        # File Writes Begin
        print("[#] Making all this data pretty...")
        line1 = 0
        writePos1 = 0
        if line1 != len(inst_recentIName_List):
            file.write(str(userSearch) + " has recently used these applications:\n")
        while line1 < len(inst_recentIName_List):
            file.write(
                "\t-'" + str(inst_recentIName_List[writePos1]) + "' from the location '" + str(
                    inst_recentIURL_List[writePos1]) + "'\n")
            line1 = line1 + 1
            writePos1 = writePos1 + 1
        file.write("\n\n")

        # Shows the user's downloads from Safari
        line1 = 0
        writePos1 = 0
        file.write(str(userSearch) + " has downloaded the following files from Safari:\n")
        while line1 < sNoTLength1:
            file.write(
                "\t-'" + str(inst_SNoT_List[writePos1]) + "' from the url '" + str(
                    inst_sURL_List[writePos1]) + "'\n")
            line1 = line1 + 1
            writePos1 = writePos1 + 1
        file.write("\n\n")

        # Shows user's Unix Executables
        line1 = 0
        writePos1 = 0
        file.write(" These are " + str(userSearch) + "'s Unix executables:\n")
        while line1 < len(inst_idn_List):
            file.write(
                "\t-'" + str(inst_idn_List[writePos1]) + "'\n" + "\t\tItem File Name: " + str(
                    inst_ifn_List[writePos1]) + "\n" + "\t\tItem Kind: " + str(
                    inst_ik_List[writePos1]) + "\n" + "\t\tPhysical Size: " + str(
                    inst_ps_List[writePos1]) + " bytes\n" + "\t\tDate it was added to this system: " + str(
                    inst_ida_List[writePos1]) + "\n" + "\t\tWhere it came from: " + str(
                    inst_iwf_List[writePos1]) + "\n")
            line1 = line1 + 1
            writePos1 = writePos1 + 1
        file.write("\n\n")

        # Shows user's Microsoft Windows Executables
        line1 = 0
        writePos1 = 0
        file.write(" These are " + str(userSearch) + "'s Microsoft Windows Executables:\n")
        while line1 < len(inst_idn2_List):
            file.write("\t-'" + str(inst_idn2_List[writePos1]) + "'\n" + "\t\tItem File Name: " + str(
                inst_ifn2_List[writePos1]) + "\n" + "\t\tItem Kind: " + str(
                inst_ik2_List[writePos1]) + "\n" + "\t\tPhysical Size: " + str(
                inst_ps2_List[writePos1]) + " bytes\n" + "\t\tDate it was added to this system: " + str(
                inst_ida2_List[writePos1]) + "\n" + "\t\tWhere it came from: " + str(
                inst_iwf2_List[writePos1]) + "\n")
            line1 = line1 + 1
            writePos1 = writePos1 + 1
        file.write("\n\n")


        # # Quarantine search requires a fuzzy name search with regex. DO NOT REMOVE FOR NOW
        # print("Counter before 18: " + str(counter))
        # if counter == 18:  # Change to if counter in 18, 19, 20
        #     y = 0
        #     while y <= sNoTLength1:
        #         print(str(counter))
        #         if counter == 18:
        #             a = tS
        #             b = q
        #             c = u
        #             g = dU
        #             h = userSearch
        #             i = inst_SNoT_List
        #         # Define Last Seen List Variables
        #         # elif counter == 3:
        #         #     a = du
        #         #     b = sls
        #         else:
        #             counter = counter + 1
        #         # SQLite Search Start
        #         cursor.execute("SELECT {} FROM {} WHERE {}=? AND {} LIKE ?".format(a, b, c, g), (h, '%' + str(i) + '%',))
        #         output = cursor.fetchall()
        #         del e[:]
        #         for (row) in output:
        #             e.append(str(row[0]))
        #         # First Seen List Start
        #         if counter == 18:
        #             print("made it to list append")
        #             inst_quarantineTimeStamp_List.append(str(e))
        #             quarantineTSLength: int = len(inst_quarantineTimeStamp_List)
        #             # if y == (volLength - 1):
        #             #     y = 0
        #             #     counter = counter + 1
        #             # else:
        #             y = y + 1

        # #     #----------------------

    #start()


    # Global Variables
    a = "None"
    b = "None"
    c = "None"
    g = "None"
    h = "None"
    i = "None"
    output = None


############# MAIN FUNCTION #############

    # Prompt user for ALL Data or just specific to User
    loop = "no"
    Y = 'Y'
    N = 'N'
    while loop == "no":
        nonUserSpecific = input("[!] Do you want to include non-user specific items for Installed Applications? [Y/N]: ")
        print("------------------------------------------------------------")
        if nonUserSpecific == Y:
            file = open(output_dir + "\\mac_int-INSTALLEDAPPS-ALL-Output.txt", 'w+')
            loop = "yes"
            generalSystem()
            userSpecificSearch()
        elif nonUserSpecific == N:
            file = open(output_dir + "\\mac_int-INSTALLEDAPPS-" + user_name +"-Output.txt", 'w+')
            userSpecificSearch()
            loop = "yes"
        else:
            print("[!] Not a valid option. Please type Y or N.\n")
            loop = "no"
    
    # Show When Parsing Completed
    if nonUserSpecific == Y:
        print("[*] Installed Application Parsing Completed!")
    else:
        print("[*] Installed Application Parsing for " + user_name + " Completed!")