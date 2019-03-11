# Query Logic for Internet Searches v1.0
# Justin Boncaldo (@boncaldoj), Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re
from var_db import *

def internetSearchRun(output_dir, input_path, user_name):
    # Output file and DB specified in mac_int.py
    file = open(output_dir + "\\mac_int-INTERNETSEARCH-" + user_name +"-Output.txt", 'w+')
    connection = sqlite3.connect(input_path)
    cursor = connection.cursor()

    # Mounted Volume variables
    global a, b, c, g, h, i, output

    def SafariQuarantine():
        global a, b, c, g, h, i, output
        # Define strings
        d = []
        e = []
        # Define counters
        end = "no"
        counter = 0
        output = None

        userSearch = user_name
        print("[#] Parsing for " + str(userSearch) + "'s Safari Data...")
        while end != "yes":
            if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                        32, 33, 34, 35):
                print("[~] Finding Safari Content...")
                while counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                                32, 33, 34, 35):
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
                    elif counter == 16:  # Searches Safari for Name, OtherInfo = SuccessfulLaunchTimestamp
                        a = NoT
                        b = S
                        c = OtherInfo
                        g = u
                        h = sLT
                        i = userSearch
                    elif counter == 17:  # Searches Safari for URL, OtherInfo = URL
                        a = url
                        b = S
                        c = OtherInfo
                        g = u
                        h = sLT
                        i = userSearch
                    elif counter == 18:  # Searches Safari for Date, OtherInfo = Date
                        a = date
                        b = S
                        c = OtherInfo
                        g = u
                        h = sLT
                        i = userSearch
                    elif counter == 19:  # Searches Safari for other Info, OtherInfo = Type
                        a = T
                        b = S
                        c = OtherInfo
                        g = u
                        h = sLT
                        i = userSearch
                    elif counter == 20:  # Searches Safari for Name, OtherInfo = Recent Searches
                        a = NoT
                        b = S
                        c = OtherInfo
                        g = u
                        h = recentsearch
                        i = userSearch
                    elif counter == 21:  # Searches Safari for URL, OtherInfo = Recent Searches
                        a = url
                        b = S
                        c = OtherInfo
                        g = u
                        h = recentsearch
                        i = userSearch
                    elif counter == 22:  # Searches Safari for Date, OtherInfo = Recent Searches
                        a = date
                        b = S
                        c = OtherInfo
                        g = u
                        h = recentsearch
                        i = userSearch
                    elif counter == 23:  # Searches Safari for Type, OtherInfo = Recent Searches
                        a = T
                        b = S
                        c = OtherInfo
                        g = u
                        h = recentsearch
                        i = userSearch
                    elif counter == 24:  # Searches Safari for Name_or_Title, Type = Topsite
                        a = NoT
                        b = S
                        c = T
                        g = u
                        h = 'TOPSITE'
                        i = userSearch
                    elif counter == 25:  # Searches Safari for URL, Type = Topsite
                        a = url
                        b = S
                        c = T
                        g = u
                        h = 'TOPSITE'
                        i = userSearch
                    elif counter == 26:  # Searches Safari for Date, Type = Topsite
                        a = date
                        b = S
                        c = T
                        g = u
                        h = 'TOPSITE'
                        i = userSearch
                    elif counter == 27:  # Searches Safari for other Info, Type = Topsite
                        a = OtherInfo
                        b = S
                        c = T
                        g = u
                        h = 'TOPSITE'
                        i = userSearch
                    elif counter == 28:  # Searches Safari for Name_or_Title, Type = Frequently Visited
                        a = NoT
                        b = S
                        c = T
                        g = u
                        h = fV
                        i = userSearch
                    elif counter == 29:  # Searches Safari for URL, Type = Frequently Visited
                        a = url
                        b = S
                        c = T
                        g = u
                        h = fV
                        i = userSearch
                    elif counter == 30:  # Searches Safari for Date, Type = Frequently Visited
                        a = date
                        b = S
                        c = T
                        g = u
                        h = fV
                        i = userSearch
                    elif counter == 31:  # Searches Safari for other Info, Type = Frequently Visited
                        a = OtherInfo
                        b = S
                        c = T
                        g = u
                        h = fV
                        i = userSearch
                    elif counter == 32:  # Searches Safari for Name, OtherInfo = Bookmarks Bar
                        a = NoT
                        b = S
                        c = OtherInfo
                        g = u
                        h = bookM
                        i = userSearch
                    elif counter == 33:  # Searches Safari for URL, OtherInfo = Bookmarks Bar
                        a = url
                        b = S
                        c = OtherInfo
                        g = u
                        h = bookM
                        i = userSearch
                    elif counter == 34:  # Searches Safari for Date, OtherInfo = Bookmarks Bar
                        a = date
                        b = S
                        c = OtherInfo
                        g = u
                        h = bookM
                        i = userSearch
                    elif counter == 35:  # Searches Safari for other Info, OtherInfo = Bookmarks Bar
                        a = T
                        b = S
                        c = OtherInfo
                        g = u
                        h = bookM
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
                        elif counter == 16:
                            internet_SafariOISLTName_List.append(string1)
                        elif counter == 17:
                            internet_SafariOISLTURL_List.append(string1)
                        elif counter == 18:
                            internet_SafariOISLTDate_List.append(string1)
                        elif counter == 19:
                            internet_SafariOISLTType_List.append(string1)
                        elif counter == 20:
                            internet_SafariOIRSName_List.append(string1)
                        elif counter == 21:
                            internet_SafariOIRSURL_List.append(string1)
                        elif counter == 22:
                            internet_SafariOIRSDate_List.append(string1)
                        elif counter == 23:
                            internet_SafariOIRSType_List.append(string1)
                        elif counter == 24:
                            internet_SafariOITSName_List.append(string1)
                        elif counter == 25:
                            internet_SafariOITSURL_List.append(string1)
                        elif counter == 26:
                            internet_SafariOITSDate_List.append(string1)
                        elif counter == 27:
                            internet_SafariOITSOther_List.append(string1)
                        elif counter == 28:
                            internet_SafariOIFVName_List.append(string1)
                        elif counter == 29:
                            internet_SafariOIFVURL_List.append(string1)
                        elif counter == 30:
                            internet_SafariOIFVDate_List.append(string1)
                        elif counter == 31:
                            internet_SafariOIFVOther_List.append(string1)
                        elif counter == 32:
                            internet_SafariOIBName_List.append(string1)
                        elif counter == 33:
                            internet_SafariOIBURL_List.append(string1)
                        elif counter == 34:
                            internet_SafariOIBDate_List.append(string1)
                        elif counter == 35:
                            internet_SafariOIBType_List.append(string1)
                        else:
                            continue
                    counter = counter + 1

            # Begins Quarantine Search
            elif counter in (36, 37, 38, 39, 40, 41):
                while counter in (36, 37, 38, 39, 40, 41):
                    if counter == 36:  # Searches Quarantine for Agent Name
                        a = aN
                        b = q
                        c = u
                        g = userSearch
                    elif counter == 37:  # # Searches Quarantine for Agent Bundle ID
                        a = aBID
                        b = q
                        c = u
                        g = userSearch
                    elif counter == 38:  # Searches Quarantine for TimeStamp
                        a = tS
                        b = q
                        c = u
                        g = userSearch
                    elif counter == 39:  # Searches Quarantine for OriginURL
                        a = oURL
                        b = q
                        c = u
                        g = userSearch
                    elif counter == 40:  # Searches Quarantine for OriginTitle
                        a = oTitle
                        b = q
                        c = u
                        g = userSearch
                    elif counter == 41:  # Searches Quarantine for Data URL
                        a = dURL
                        b = q
                        c = u
                        g = userSearch

                    else:
                        print("A counting error has occurred")

                    cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c,), (g,))
                    output = cursor.fetchall()
                    del d[:]
                    for row in output:
                        d.append(str(row[0]))
                    pos = 0
                    for (row) in output:
                        string1 = str(d[pos])
                        pos = pos + 1
                        # Volume Name List Start
                        if counter == 36:
                            internet_QuarantineName_List.append(string1)
                        elif counter == 37:
                            internet_QuarantineABID_List.append(string1)
                        elif counter == 38:
                            internet_QuarantineTS_List.append(string1)
                        elif counter == 39:
                            internet_QuarantineOURL_List.append(string1)
                        elif counter == 40:
                            internet_QuarantineOTitle_List.append(string1)
                        elif counter == 41:
                            internet_QuarantineDURL_List.append(string1)
                        else:
                            continue
                    counter = counter + 1



            else:
                end = "yes"

                # Safari Write, OtherInfo = SuccessfulLaunchTimestamp
                line1 = 0
                writePos1 = 0
                if line1 != len(internet_SafariOISLTName_List):
                    file.write(str(userSearch) + " last launched Safari on ")
                else:
                    file.write(str(userSearch) + " has not launched Safari\n")
                while line1 < len(internet_SafariOISLTName_List):
                    file.write(str(internet_SafariOISLTDate_List[writePos1]) + "\n\n")
                    line1 = line1 + 1
                    writePos1 = writePos1 + 1
                file.write("\n\n")

                # Safari Write, Type = Download
                line1 = 0
                writePos1 = 0
                if line1 != len(internet_SafariDLName_List):
                    file.write(str(userSearch) + " has the following Downloads from Safari:\n")
                else:
                    file.write(str(userSearch) + " has not downloaded anything on Safari\n")
                while line1 < len(internet_SafariDLName_List):
                    file.write("\t-'" + str(internet_SafariDLName_List[writePos1]) + "' from the location '" + str(
                        internet_SafariDLURL_List[writePos1]) + "'\n\t\tDate: " + str(
                        internet_SafariDLDate_List[writePos1]) + "\n\t\tSave Location: " + str(
                        internet_SafariDLOther_List[writePos1]) + "\n\n")
                    line1 = line1 + 1
                    writePos1 = writePos1 + 1
                file.write("\n\n")

                # Quarantine Write
                line1 = 0
                writePos1 = 0
                if line1 != len(internet_QuarantineName_List):
                    file.write(str(userSearch) + " had the following downloads pass through Quarantine:\n")
                else:
                    file.write(str(userSearch) + " had no downloads pass through Quarantine\n")
                while line1 < len(internet_QuarantineName_List):
                    file.write("\t-Browser: '" + str(internet_QuarantineName_List[writePos1]) + "' on '" + str(
                        internet_QuarantineTS_List[writePos1]) + "'\n\t\tOrigin Title: " + str(
                        internet_QuarantineOTitle_List[writePos1]) + "\n\t\tOrigin URL: " + str(
                        internet_QuarantineOURL_List[writePos1]) + "\n\t\tData URL: " + str(
                        internet_QuarantineDURL_List[writePos1]) + "\n\t\tAgent Bundle ID: " + str(
                        internet_QuarantineABID_List[writePos1]) + "\n\n")
                    line1 = line1 + 1
                    writePos1 = writePos1 + 1
                file.write("\n\n")

                # Safari Write, OtherInfo = Recent Searches
                line1 = 0
                writePos1 = 0
                if line1 != len(internet_SafariOIRSName_List):
                    file.write(str(userSearch) + " made the following recent searches on Safari:\n")
                else:
                    file.write(str(userSearch) + " made no recent searches on Safari\n")
                while line1 < len(internet_SafariOIRSName_List):
                    file.write("\t-'" + str(internet_SafariOIRSName_List[writePos1]) + "' on " + str(
                        internet_SafariOIRSDate_List[writePos1]) + "'\n\t\tType: " + str(
                        internet_SafariOIRSType_List[writePos1]) + "\n\n")
                    line1 = line1 + 1
                    writePos1 = writePos1 + 1
                file.write("\n\n")

                # Safari Write, Type = Frequently Visited
                line1 = 0
                writePos1 = 0
                if line1 != len(internet_SafariOIFVName_List):
                    file.write("These are " + str(userSearch) + "'s most frequently sites on Safari:\n")
                else:
                    file.write(str(userSearch) + " has no frequently visited sites on Safari\n")
                while line1 < len(internet_SafariOIFVName_List):
                    file.write("\t-'" + str(internet_SafariOIFVName_List[writePos1]) + "' at the URL '" + str(
                        internet_SafariOIFVURL_List[writePos1]) + "'\n\t\tDate: " + str(
                        internet_SafariOIFVDate_List[writePos1]) + "\n\t\tOther Info: " + str(
                        internet_SafariOIFVOther_List[writePos1]) + "\n\n")
                    line1 = line1 + 1
                    writePos1 = writePos1 + 1
                file.write("\n\n")

                # Safari Write, Type = TOPSITES
                line1 = 0
                writePos1 = 0
                if line1 != len(internet_SafariOITSName_List):
                    file.write("These are " + str(userSearch) + "'s top sites on Safari:\n")
                else:
                    file.write(str(userSearch) + " has no top sites on Safari\n")
                while line1 < len(internet_SafariOITSName_List):
                    file.write("\t-'" + str(internet_SafariOITSName_List[writePos1]) + "' at the URL '" + str(
                        internet_SafariOITSURL_List[writePos1]) + "'\n\t\tDate: " + str(
                        internet_SafariOITSDate_List[writePos1]) + "\n\t\tOther Info: " + str(
                        internet_SafariOITSOther_List[writePos1]) + "\n\n")
                    line1 = line1 + 1
                    writePos1 = writePos1 + 1
                file.write("\n\n")

                # Safari Write, Type = LastSession
                line1 = 0
                writePos1 = 0
                if line1 != len(internet_SafariLSName_List):
                    file.write(str(userSearch) + " had these URLs auto-launch from their last closed Safari session:\n")
                else:
                    file.write(str(userSearch) + " has no Safari searches saved from their last session\n")
                while line1 < len(internet_SafariLSName_List):
                    file.write("\t-'" + str(internet_SafariLSName_List[writePos1]) + "' from the location '" + str(
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
                    file.write("\t-'" + str(internet_SafariRCName_List[writePos1]) + "' from the location '" + str(
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
                    file.write("\t-'" + str(internet_SafariHName_List[writePos1]) + "' with the URL '" + str(
                        internet_SafariHURL_List[writePos1]) + "'\n\t\tDate: " + str(
                        internet_SafariHDate_List[writePos1]) + "\n\t\tOther Info: " + str(
                        internet_SafariHOther_List[writePos1]) + "\n\n")
                    line1 = line1 + 1
                    writePos1 = writePos1 + 1
                file.write("\n\n")

                # Safari Write, OtherInfo = Bookmarks Bar
                line1 = 0
                writePos1 = 0
                if line1 != len(internet_SafariOIBName_List):
                    file.write(str(userSearch) + " has the following Bookmarks on Safari:\n")
                else:
                    file.write(str(userSearch) + " has no Bookmarks on Safari\n")
                while line1 < len(internet_SafariOIBName_List):
                    file.write("\t-'" + str(internet_SafariOIBName_List[writePos1]) + "'\n\t\tType: " + str(
                        internet_SafariOIBType_List[writePos1]) + "\n\n")
                    line1 = line1 + 1
                    writePos1 = writePos1 + 1
                file.write("\n\n")


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

    ############# MAIN FUNCTION #############

    # Run SAFARI Parsing
    SafariQuarantine()

    # Show When Parsing Completed
    print("[#] Making all this data pretty...")
    print("[*] Internet Search Parsing Completed!")
