# Query Logic for Internet searches v0.1
# Justin Boncaldo (@boncaldoj) 2019
# ----------------------------------------------------------

import sqlite3
import re
from variable_db import *


# Specify files here for testing
#file = open('/Users/zachburnham/Desktop/Capstone/Mac_apt_Output/exampleWrite.txt', 'w+')
#connection = sqlite3.connect('/Users/zachburnham/Desktop/Capstone/Mac_apt_Output/mac_apt02.db')
file = open('E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\exampleWrite.txt', 'w+')
connection = sqlite3.connect('E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\mac_apt02.db')


cursor = connection.cursor()

# Mounted Volume variables
global a, b, c, g, h, i, output

def Safari():
    global a, b, c, g, h, i, output
    # Define strings
    d = []
    e = []
    # Define counters
    end = "no"
    counter = 0
    output = None

    userSearch = input("What User? (Enter for default All): ")
    print("Starting Parsing " + str(userSearch) + "'s Safari Data...")
    while end != "yes":
        if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
            print("[~] Finding Safari Content...")
            while counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
                # 0 -
                if counter == 0:  # Searches Safari for Name_or_Title, Type = Download
                    a = NoT
                    b = S
                    c = T
                    g = u
                    h = dL
                    i = userSearch
                elif counter == 1:  # Searches Safari for URL, Type = Download
                    a = url
                    b = S
                    c = T
                    g = u
                    h = dL
                    i = userSearch
                elif counter == 2:  # Searches Safari for URL, Type = Date
                    a = date
                    b = S
                    c = T
                    g = u
                    h = dL
                    i = userSearch
                elif counter == 3:  # Searches Safari for Download Location with Other_Info, Type = Date
                    a = OtherInfo
                    b = S
                    c = T
                    g = u
                    h = dL
                    i = userSearch
                elif counter == 4:  # Searches Safari for Name_or_Title, Type = LastSession
                    a = NoT
                    b = S
                    c = T
                    g = u
                    h = LastSession
                    i = userSearch
                elif counter == 5:  # Searches Safari for URL, Type = LastSession
                    a = url
                    b = S
                    c = T
                    g = u
                    h = LastSession
                    i = userSearch
                elif counter == 6:  # Searches Safari for Date, Type = LastSession
                    a = date
                    b = S
                    c = T
                    g = u
                    h = LastSession
                    i = userSearch
                elif counter == 7:  # Searches Safari for other Info, Type = LastSession
                    a = OtherInfo
                    b = S
                    c = T
                    g = u
                    h = LastSession
                    i = userSearch
                elif counter == 8:  # Searches Safari for Name_or_Title, Type = Recently Closed
                    a = NoT
                    b = S
                    c = T
                    g = u
                    h = recentlyClosed
                    i = userSearch
                elif counter == 9:  # Searches Safari for URL, Type = Recently Closed
                    a = url
                    b = S
                    c = T
                    g = u
                    h = recentlyClosed
                    i = userSearch
                elif counter == 10:  # Searches Safari for Date, Type = Recently Closed
                    a = date
                    b = S
                    c = T
                    g = u
                    h = recentlyClosed
                    i = userSearch
                elif counter == 11:  # Searches Safari for other Info, Type = Recently Closed
                    a = OtherInfo
                    b = S
                    c = T
                    g = u
                    h = recentlyClosed
                    i = userSearch

                elif counter == 12:  # Searches Safari for Name_or_Title, Type = History
                    a = NoT
                    b = S
                    c = T
                    g = u
                    h = 'HISTORY'
                    i = userSearch
                elif counter == 13:  # Searches Safari for URL, Type = History
                    a = url
                    b = S
                    c = T
                    g = u
                    h = 'HISTORY'
                    i = userSearch
                elif counter == 14:  # Searches Safari for Date, Type = History
                    a = date
                    b = S
                    c = T
                    g = u
                    h = 'HISTORY'
                    i = userSearch
                elif counter == 15:  # Searches Safari for other Info, Type = History
                    a = OtherInfo
                    b = S
                    c = T
                    g = u
                    h = 'HISTORY'
                    i = userSearch
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
                    # Volume Name List Start
                    if counter == 0:
                        internet_SafariDLName_List.append(string1)
                    elif counter == 1:
                        internet_SafariDLURL_List.append(string1)
                    elif counter == 2:
                        internet_SafariDLDate_List.append(string1)
                    elif counter == 3:
                        internet_SafariDLOther_List.append(string1)
                    elif counter == 4:
                        internet_SafariLSName_List.append(string1)
                    elif counter == 5:
                        internet_SafariLSURL_List.append(string1)
                    elif counter == 6:
                        internet_SafariLSDate_List.append(string1)
                    elif counter == 7:
                        internet_SafariLSOther_List.append(string1)
                    elif counter == 8:
                        internet_SafariRCName_List.append(string1)
                    elif counter == 9:
                        internet_SafariRCURL_List.append(string1)
                    elif counter == 10:
                        internet_SafariRCDate_List.append(string1)
                    elif counter == 11:
                        internet_SafariRCOther_List.append(string1)
                    elif counter == 12:
                        internet_SafariHName_List.append(string1)
                    elif counter == 13:
                        internet_SafariHURL_List.append(string1)
                    elif counter == 14:
                        internet_SafariHDate_List.append(string1)
                    elif counter == 15:
                        internet_SafariHOther_List.append(string1)
                    else:
                        continue
                counter = counter + 1

        else:
            end = "yes"

            # Safari Write, Type = Download
            line1 = 0
            writePos1 = 0
            if line1 != len(internet_SafariDLName_List):
                file.write(str(userSearch) + " has the following Downloads from Safari:\n")
            else:
                file.write(str(userSearch) + " has no Safari internet activity\n")
            while line1 < len(internet_SafariDLName_List):
                file.write("\t•'" + str(internet_SafariDLName_List[writePos1]) + "' from the location '" + str(
                    internet_SafariDLURL_List[writePos1]) + "'\n\t\tDate: " + str(
                    internet_SafariDLDate_List[writePos1]) + "\n\t\tSave Location: " + str(
                    internet_SafariDLOther_List[writePos1]) + "\n\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Safari Write, Type = LastSession
            line1 = 0
            writePos1 = 0
            if line1 != len(internet_SafariLSName_List):
                file.write(str(userSearch) + " had these URLs saved from their last Safari session:\n")
            else:
                file.write(str(userSearch) + " has no saved Safari searches from their last session\n")
            while line1 < len(internet_SafariLSName_List):
                file.write("\t•'" + str(internet_SafariLSName_List[writePos1]) + "' from the location '" + str(
                    internet_SafariLSURL_List[writePos1]) + "'\n\t\tDate: " + str(
                    internet_SafariLSDate_List[writePos1]) + "\n\t\tSave Location: " + str(
                    internet_SafariLSOther_List[writePos1]) + "\n\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Safari Write, Type = RecentlyClosedTab
            line1 = 0
            writePos1 = 0
            if line1 != len(internet_SafariRCName_List):
                file.write(str(userSearch) + " has recently closed these Safari tabs:\n")
            else:
                file.write(str(userSearch) + " has not recently closed any Safari tabs\n")
            while line1 < len(internet_SafariRCName_List):
                file.write("\t•'" + str(internet_SafariRCName_List[writePos1]) + "' from the location '" + str(
                    internet_SafariRCURL_List[writePos1]) + "'\n\t\tDate: " + str(
                    internet_SafariRCDate_List[writePos1]) + "\n\t\tOther Info: " + str(
                    internet_SafariRCOther_List[writePos1]) + "\n\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")

            # Safari Write, Type = History
            line1 = 0
            writePos1 = 0
            if line1 != len(internet_SafariHName_List):
                file.write(str(userSearch) + " has the following Safari search history:\n")
            else:
                file.write(str(userSearch) + " has no Safari search history\n")
            while line1 < len(internet_SafariHName_List):
                file.write("\t•'" + str(internet_SafariHName_List[writePos1]) + "' with the URL '" + str(
                    internet_SafariHURL_List[writePos1]) + "'\n\t\tDate: " + str(
                    internet_SafariHDate_List[writePos1]) + "\n\t\tOther Info: " + str(
                    internet_SafariHOther_List[writePos1]) + "\n\n")
                line1 = line1 + 1
                writePos1 = writePos1 + 1
            file.write("\n\n")


Safari()

# elif counter in (10, 11, 12, 13, 14, 15, 16, 17):
#     print("[~] Finding User Downloads...")
#     while counter in (10, 11, 12, 13, 14, 15, 16, 17):
#         if counter == 10:
#             a = n
#             b = ri
#             c = T
#             g = u
#             h = application
#             i = userSearch
#             print("A counting error has occurred")
#
#         cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
#         output = cursor.fetchall()
#         del d[:]
#         for row in output:
#             d.append(str(row[0]))
#         pos = 0
#         for (row) in output:
#             string1 = str(d[pos])
#             pos = pos + 1
#             # Volume Name List Start
#             if counter == 10:
#                 user_recentIName_List.append(string1)
#                 user_riNLength1: int = len(user_recentIName_List)
#             else:
#                 continue
#         counter = counter + 1

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
